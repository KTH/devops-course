#!/usr/bin/env python3

import re
import time
import sys
import shutil
import math
import subprocess
import tempfile
import Levenshtein as lev

from os import listdir, makedirs, removedirs
from collections import defaultdict
from itertools import combinations
from functools import reduce
from operator import add
from os.path import isdir, isfile, islink, exists, join, realpath, abspath, basename

start_time = 0

def printl(msg, library = None, end = '\n', pre=''):
    exec_time = time.time() - start_time
    print("{}[{:03.0f}s{}] {}".format(pre, exec_time, "|" + library if library is not None else "", msg), end=end)

def assertValidOutputDirectory(output_dir):
    if exists(output_dir) and not isdir(output_dir):
        print("Output directory {} does already exist and is not a directory"
                .format(output_dir), file=sys.stderr)
        sys.exit(1)
    if not exists(output_dir):
        makedirs(output_dir)

def setupLibrary(executable, output_directory):
    output = subprocess.run([executable], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    library = re.findall(r'Executing library: ([a-zA-Z\-]+)', output.stdout.decode('utf-8').splitlines()[0])[0]
    if len(library) <= 3: # probably a bug then
        print("Unable to parse json library in use.", file=sys.stderr)
        print("Recieved: \"{}\"".format(library), file=sys.stderr)
        sys.exit(1)
    directory_path = join(output_directory, library)
    assertValidOutputDirectory(directory_path)
    return (library, directory_path)

def addFile(path):
    if exists(path):
        if isdir(path):
            return reduce(lambda files,f: files + addFile(join(path, f)), listdir(path), [])
        if isfile(path):
            return [abspath(path)]
        if islink(path):
            return addFile(realpath(path))
    return []

def main():
    global start_time
    start_time = time.time()
    test_cases = list(addFile(sys.argv[1]))
    num_inputs = len(test_cases)
    printl("Found {} test cases".format(num_inputs))

    output_dir = abspath(sys.argv[2])
    assertValidOutputDirectory(output_dir)

    library_stats = {}
    executables = sys.argv[3:]
    max_library_name = max(map(len, map(basename, executables)))

    executables.sort()
    library_counter = 0
    total_crashes = 0

    for executable in executables:
        library_name, library_dir = setupLibrary(abspath(executable), output_dir)
        library = library_name.rjust(max_library_name)
        library_counter += 1
        stderrors = []
        index = 0
        crashes = 0
        index_padding = "{{:>{}}}".format(math.floor(math.log10(num_inputs)) + 1)
        progress_format = "{0}/{0}".format(index_padding)

        for test_case in test_cases:

            # Progress report
            index += 1
            percent = round(100 * index / num_inputs, 2)
            printl("Classifying crashes: "
                  + index_padding.format(crashes)
                  + " [".format(crashes)
                  + progress_format.format(index, num_inputs)
                  + " {:05.2f}%]".format(percent)
                  , library=library
                  , end=''
                  , pre='\r')

            crashes += 1
            bug_dir = join(library_dir, str(crashes))
            assertValidOutputDirectory(bug_dir)

            with open(join(bug_dir, "stdout.txt"), 'wb') as stdout_log:

                # Run the json parsing executable
                test = subprocess.Popen([executable, test_case]
                                       , stdout=stdout_log
                                       , stderr=subprocess.PIPE
                                       , env={"ASAN_OPTIONS": "detect_leaks=0:log_path=" + join(bug_dir, "asan.log")})

            _, stderr = test.communicate()

            # check if it crashed
            if test.returncode == 0 and len(stderr) == 0:
                crashes -= 1
                shutil.rmtree(bug_dir, ignore_errors=True)
                continue


            # Save the sanitizer log aswell as a copy of the crashing input
            shutil.copy2(test_case, join(bug_dir, "input.json"))
            stderrors.append(stderr)

            with open(join(bug_dir, "stderr.txt"), 'wb') as stderr_log:
                stderr_log.write(stderr)


        print()
        total_crashes += crashes
        if crashes == 0:
            shutil.rmtree(library_dir, ignore_errors=True)
            continue

        # duplicates not implemented yet
        library_stats[library] = (crashes, 0)

        # Attempts to deduplicate the crashing inputs based on levenshtein ratio on stderr
        # Too slow atm
        #printl("Deduplicating crashes...", library=library, end='\r', pre='\n')
        #duplicates = defaultdict(list)
        #duplicate_count = 0
        #for i, j in combinations(range(len(stderrors)), 2):
        #    # TODO? improve this heuristic
        #    if len(stderrors[i]) > 5 and len(stderrors[j]) > 5 \
        #        and lev.ratio(stderrors[i], stderrors[j]) >= 0.80:
        #        duplicates[i + 1].append(j + 1)
        #        duplicate_count += 1

        #library_stats[library] = (crashes, duplicate_count)
        #if duplicate_count == 0:
        #    continue

        #printl("Found {} suspected duplicates".format(duplicate_count), library=library)
        #with open(join(library_dir, "duplicates.txt"), 'w') as duplicates_file:
        #    for bug in duplicates:
        #        output = "Bug #{}: {}".format(bug, ", ".join(map(index_padding.format, duplicates[bug])))
        #        print(output, file=duplicates_file)


    if total_crashes == 0:
        return
    # print a formatted table sorted on number the of crashes per library, in descending order
    print("\nCrashes found in {} out of {} given inputs".format(total_crashes, num_inputs))
    crashing_libs = sorted(library_stats.keys(), key=lambda lib: library_stats[lib][1])
    longest_crashing_name = max(map(len, crashing_libs))
    table_cell = "{{:>{}}}".format(max(5, math.log10(num_inputs)))
    print("lib".rjust(longest_crashing_name + 1)
          + "  " + table_cell.format("crash")
          + " "  + table_cell.format("dupes")
          + " "  + table_cell.format("uniqs")
          + " "  + table_cell.format("%"))
    for lib in crashing_libs:
        crashes, dupes = library_stats[lib]
        percent = round(100 * crashes / num_inputs, 2)
        print(lib.rjust(longest_crashing_name + 1)
              + ": " + table_cell.format(crashes)
              + " "  + table_cell.format(dupes)
              + " "  + table_cell.format(crashes - dupes)
              + " "  + table_cell.format(percent))

    print()
    printl("All output written to: {}".format(output_dir))

if __name__ == '__main__':
    main()
