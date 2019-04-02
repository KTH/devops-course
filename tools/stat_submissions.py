#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: stat_submissions.py

import sys, os, time, logging
import getopt
from prettytable import PrettyTable

SUBMISSIONS_PATH = ''
PRINT_STUDENT_STAT = False

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
    
    print("Statistic Information for Each Category")
    print_stat_category(stat_per_category)

    if PRINT_STUDENT_STAT:
        print("Statistic Information for Each Student")
        print_stat_student(stat_per_student)

def print_stat_category(stat_info):
    stat_table = PrettyTable()
    stat_table.field_names = ["Category name", "Submissions"]

    total = 0
    for category in stat_info:
        stat_table.add_row([category, stat_info[category]["task_count"]])
        total = total + stat_info[category]["task_count"]
    stat_table.add_row(["TOTAL", total])

    print(stat_table)

def print_stat_student(stat_info):
    stat_table = PrettyTable()
    stat_table.field_names = ["Index", "Student name", "Submissions Count", "Categories"]

    index = 1
    for student in stat_info:
        stat_table.add_row([index, student, len(stat_info[student]), " ".join(stat_info[student])])
        index = index + 1

    print(stat_table)

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

    try:
        opts, args = getopt.getopt(argv, "p:", ["path=", "printStudentStat", "help"])
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
    print('stat_submissions.py --help to display this help info')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()