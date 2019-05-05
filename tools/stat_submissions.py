#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: stat_submissions.py

import sys, os, time, logging
import getopt
from prettytable import PrettyTable

SUBMISSIONS_PATH = ''
PRINT_STUDENT_STAT = False
PRINT_IN_MARKDOWN = False

def main():
    handle_args(sys.argv[1:])

    stat_per_category = stat_categories(SUBMISSIONS_PATH)
    stat_per_student = dict()

    for category in stat_per_category:
        names = stat_students(category, stat_per_category[category]["path"])
        for name in names:
            if name not in stat_per_student:
                stat_per_student.update({name:[category]})
            else:
                stat_per_student[name].append(category)
    print("*Automatically genereated at %s*"%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    print("Statistic Information for Each Category")
    print("")
    print_stat_category_markdown(stat_per_category) if PRINT_IN_MARKDOWN else print_stat_category(stat_per_category)
    print("")

    if PRINT_STUDENT_STAT:
        print("Statistic Information for Each Student")
        print("")
        print_stat_student_markdown(stat_per_student) if PRINT_IN_MARKDOWN else print_stat_student(stat_per_student)

def print_stat_category(stat_info):
    stat_table = PrettyTable()
    stat_table.field_names = ["Category name", "Registrations"]

    total = 0
    for category in stat_info:
        stat_table.add_row([category, stat_info[category]["task_count"]])
        total = total + stat_info[category]["task_count"]
    stat_table.add_row(["TOTAL", total])

    print(stat_table)

def print_stat_category_markdown(stat_info):
    print("|Category name | Registrations|")
    print("|--------------|--------------|")
    total = 0
    for category in stat_info:
        print("|%s|%s|"%(category, stat_info[category]["task_count"]))
        total = total + stat_info[category]["task_count"]
    print("|--------------|------------|")
    print("|TOTAL|%s|"%total)


def print_stat_student(stat_info):
    stat_table = PrettyTable()
    stat_table.field_names = ["Index", "Student name", "Registrations Count", "Categories"]

    index = 1
    summary = {5:[], 4:[], 3:[], 2:[], 1:[]}
    for student in stat_info:
        task_count = len(stat_info[student])
        stat_table.add_row([index, student, task_count, " ".join(stat_info[student])])
        summary[task_count].append(student)
        index = index + 1

        if task_count > 4:
            logging.warn("%s's task_count is: %d (> 4)"%(student, task_count))

    print(stat_table)

    print("")
    print("Summary")
    for count in summary:
        print("%s students with %s registered tasks: %s"%(len(summary[count]), count, ", ".join(summary[count])))

def print_stat_student_markdown(stat_info):
    print("|Index | Student name | Registrations Count | Categories|")
    print("|------|--------------|---------------------|-----------|")

    index = 1
    summary = {4:[], 3:[], 2:[], 1:[]}
    for student in stat_info:
        task_count = len(stat_info[student])
        print("|%s|%s|%s|%s|"%(index, student, task_count, " ".join(stat_info[student])))
        summary[task_count].append(student)
        index = index + 1

        # if task_count >= 4:
        #     logging.warn("%s's task_count >= 4"%student)

    print("")
    print("Summary")
    for count in summary:
        print("**%s students with %s registered tasks:** %s"%(len(summary[count]), count, ", ".join(summary[count])))

def stat_categories(path):
    categories = dict()

    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        for category in dirnames:
            categories[category] = {"path":os.path.join(dirpath, category), "task_count":0}
        break

    for category in categories:
        for dirpath, dirnames, filenames in os.walk(categories[category]["path"], topdown=True):
            if (category == "presentation"):
                if dirpath[-5:-1] == "week":
                    categories[category][dirpath[-5:]] = len(dirnames)
                    categories[category]["task_count"] = categories[category]["task_count"] + len(dirnames)
            else:
                categories[category]["task_count"] = len(dirnames)
                break

    return categories

def stat_students(category, path):
    student_names = list()

    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        if (category == "presentation"):
            if dirpath[-5:-1] == "week":
                for folder in dirnames:
                    for x in folder.split("-"):
                        student_names.append(x)
        else:
            # any better expressions to achieve this?
            for folder in dirnames:
                for x in folder.split("-"):
                    student_names.append(x)
            break

    return student_names

def handle_args(argv):
    global SUBMISSIONS_PATH
    global PRINT_STUDENT_STAT
    global PRINT_IN_MARKDOWN

    try:
        opts, args = getopt.getopt(argv, "p:m", ["path=", "printStudentStat", "printInMarkdown", "help"])
    except getopt.GetoptError as error:
        logging.error(error)
        print_help_info()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "--help":
            print_help_info()
            sys.exit()
        elif opt in ("-p", "--path"):
            SUBMISSIONS_PATH = arg
        elif opt in ("--printStudentStat"):
            PRINT_STUDENT_STAT = True
        elif opt in ("-m", "--printInMarkdown"):
            PRINT_IN_MARKDOWN = True

    if SUBMISSIONS_PATH == '':
        logging.error("You should use -p or --path= to specify the path to students submissions")
        print_help_info()
        sys.exit(2)

def print_help_info():
    print('')
    print('DD2482 Student Submissions Statistic Tool')
    print('    stat_submissions.py -p <submissions_folder_path>')
    print('or: stat_submissions.py --path=<submissions_folder_path>')
    print('')
    print('optional:')
    print('    --printStudentStat print statistic data per student')
    print('    -m or --printInMarkdown print statistic data in markdown syntax')
    print('stat_submissions.py --help to display this help info')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
