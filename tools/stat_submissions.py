#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: stat_submissions.py

import sys, os, time, logging
import getopt
from github import Github
from prettytable import PrettyTable

SUBMISSIONS_PATH = ''
PRINT_STUDENT_STAT = False
PRINT_IN_MARKDOWN = False
PUBLISH = False

# ENVs for publishing the results
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_FULLNAME = os.getenv("REPO_FULLNAME")
ISSUE_NUMBER = os.getenv("ISSUE_NUMBER")

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

    content = ""
    content = content + "*Automatically genereated at %s*\n"%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    content = content + "Statistic Information for Each Category\n"

    if PRINT_IN_MARKDOWN:
        content = content + get_stat_category_markdown(stat_per_category)
    else:
        content = content + get_stat_category(stat_per_category)

    if PRINT_STUDENT_STAT:
        content = content + "\nStatistic Information for Each Student\n"
        if PRINT_IN_MARKDOWN:
            content = content + get_stat_student_markdown(stat_per_student)
        else:
            content = content + get_stat_student(stat_per_student)

    if PUBLISH:
        publish_on_issue(content)
    else:
        print (content)

def publish_on_issue(content):
    github = Github(GITHUB_TOKEN)
    gitrepo = github.get_repo(REPO_FULLNAME)
    if ISSUE_NUMBER != "" and int(ISSUE_NUMBER) > 0:
        issue = gitrepo.get_issue(number = int(ISSUE_NUMBER))
        issue.edit(body = content)


def get_stat_category(stat_info):
    stat_table = PrettyTable()
    stat_table.field_names = ["Category name", "Registrations"]

    total = 0
    for category in stat_info:
        stat_table.add_row([category, stat_info[category]["task_count"]])
        total = total + stat_info[category]["task_count"]
    stat_table.add_row(["TOTAL", total])

    return stat_table.get_string()

def get_stat_category_markdown(stat_info):
    return_str = """
|Category name | Registrations|
|--------------|--------------|
"""
    total = 0
    for category in stat_info:
        return_str = return_str + "|%s|%s|\n"%(category, stat_info[category]["task_count"])
        total = total + stat_info[category]["task_count"]
    return_str = return_str + "|--------------|------------|\n"
    return_str = return_str + "|TOTAL|%s|\n"%total

    return return_str


def get_stat_student(stat_info):
    stat_table = PrettyTable()
    stat_table.field_names = ["Index", "Student name", "Registrations Count", "Categories"]

    index = 1
    summary = {5:[], 4:[], 3:[], 2:[], 1:[]}
    for student in stat_info:
        task_count = len(stat_info[student])
        stat_table.add_row([index, student, task_count, " ".join(stat_info[student])])
        summary[task_count].append(student)
        index = index + 1

        if task_count > 5:
            logging.warn("%s's task_count is: %d (> 5)"%(student, task_count))

    return_str = stat_table.get_string()

    return_str = return_str + "\nSummary\n"
    for count in summary:
        return_str = return_str + "%s students with %s registered tasks: %s\n"%(len(summary[count]), count, ", ".join(summary[count]))

    return return_str

def get_stat_student_markdown(stat_info):
    return_str = """
|Index | Student name | Registrations Count | Categories|
|------|--------------|---------------------|-----------|
"""

    index = 1
    summary = {5:[], 4:[], 3:[], 2:[], 1:[]}
    for student in stat_info:
        task_count = len(stat_info[student])
        return_str = return_str + "|%s|%s|%s|%s|\n"%(index, student, task_count, " ".join(stat_info[student]))
        summary[task_count].append(student)
        index = index + 1

        # if task_count >= 4:
        #     logging.warn("%s's task_count >= 4"%student)

    return_str = return_str + "\nSummary\n"
    for count in summary:
        return_str = return_str + "**%s students with %s registered tasks:** %s\n"%(len(summary[count]), count, ", ".join(summary[count]))

    return return_str

def stat_categories(path):
    categories = dict()

    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        for category in dirnames:
            categories[category] = {"path":os.path.join(dirpath, category), "task_count":0}
        break

    for category in categories:
        for dirpath, dirnames, filenames in os.walk(categories[category]["path"], topdown=True):
            if (category == "presentation" or category == "demo"):
                if dirpath.split("/")[-1].startswith("week"):
                    # if we are in a weekX folder
                    categories[category][dirpath.split("/")[-1][:5]] = len(dirnames)
                    categories[category]["task_count"] = categories[category]["task_count"] + len(dirnames)
            else:
                categories[category]["task_count"] = len(dirnames)
                break

    return categories

def stat_students(category, path):
    student_names = list()

    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        if (category == "presentation" or category == "demo"):
            if dirpath.split("/")[-1].startswith("week"):
                # if we are in a weekX folder
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
    global PUBLISH

    try:
        opts, args = getopt.getopt(argv, "p:m", ["path=", "printStudentStat", "printInMarkdown", "publish", "help"])
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
        elif opt in ("--publish"):
            PUBLISH = True

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
    print('    --publish publish the statistics on an issue')
    print('stat_submissions.py --help to display this help info')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
