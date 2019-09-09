from option import Option
from fractions import Fraction

import os
import subprocess
import random
import string
import yaml
import re

class Util:
    def __init__(self, name):
        self.name = name
        self.noOfArgs = [0]
        self.readOptionsFromYaml()
        self.addCommonOptions()
    
    def fuzz(self):
        rand_opts = self.getRandomOptions()
        opts = []
        opts.append(list(map(lambda x: x.randomizeAndFormat(), rand_opts)))
        return opts

    def execute(self, args):
        args.insert(0, "src/" + self.name)
        subprocess.run(args
                      , cwd="/home/fuzz/coreutils"
                      , stderr=subprocess.PIPE
                      , stdout=subprocess.PIPE)

    
    def getRandomArgs(self):
        # Existing files
        k = random.randint(0, 10) if self.noOfArgs == "list" else random.choice(self.noOfArgs)
        k = random.randint(k - 1, k + 1)
        args = [os.path.join(dp, f) for dp, dn, filenames in os.walk("files") for f in filenames]
        
        # Non-existing files
        for _ in range (4):
            args.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=20)))
        
        return random.choices(args, k=k)
    
    def getRandomOptions(self):
        n = random.randint(0, len(self.options) - 1)
        return list(random.sample(self.options, n))
        
    def addCommonOptions(self):
        help = Option(["--help"], "{}")
        version = Option(["--version"], "{}")
        self.options.add(help)
        self.options.add(version)

    def readOptionsFromYaml(self):
        with open ("data/coreutils_options.yaml", "r") as f:
            full_yaml = yaml.safe_load(f)
            util_yaml = full_yaml[self.name]

            self.options = set()

            if util_yaml == None:
                return
            
            self.paramFormat = util_yaml["paramFormat"]
            self.optionFormat = util_yaml["optionFormat"]
            self.noOfArgs = util_yaml["noOfArgs"]
            
            for option in util_yaml["options"]:
                if isinstance(option, list):    # no parameters
                    names = option
                    params = None
                else:                           # parameters
                    names = [list(option.keys())[0]]
                    params = list(option.values())[0]
                
                self.options.add(Option(names, self.optionFormat, self.paramFormat, params))

    def getCoverage(self):
        stdout = subprocess.run(['gcov', 'src/' + self.name]
                                , stdout=subprocess.PIPE
                                , stderr=subprocess.PIPE
                                , cwd="/home/fuzz/coreutils").stdout.decode('utf-8')
        lines = re.findall("Lines executed:(\d+\.\d+)% of (\d+)", stdout)
        total_lines = 0
        total_coverage = 0
        for line in lines:
            file_length = int(line[1])
            percentage = float(line[0]) / 100
            total_lines += file_length
            total_coverage += round(percentage * file_length)
                
        return (total_coverage, total_lines)

    def generateReport():
        subprocess.call(["lcov", "--capture", "--directory", "/home/fuzz/coreutils/src", "--output-file", "/tmp/coverage.info"])
        subprocess.call(["genhtml", "/tmp/coverage.info", "--output-directory", "/proj/report"])