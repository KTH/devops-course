#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: missing_grade.py
import json, os
import argparse, requests
import sys

TASK = ''
WEEK = ''
DEADLINE = 0
CANVAS_TOKEN = ''
CANVAS_URL = "https://canvas.kth.se"
CANVAS_COURSE_ID = 31421
CONTRIBUTION_PATH = '../contributions'


# Mapping from github task name to canvas group set id
def task_to_set(task_name, canvas_set):
    mapping = {
        "course-automation": canvas_set["Course automation"],
        "demo": canvas_set["Demos"],
        "essay": canvas_set["Essays"],
        "executable-tutorial": canvas_set["Executable Tutorials"],
        "feedback": canvas_set["Feedback"],
        "open-source": canvas_set["Open-source contributions"],
        "presentation": canvas_set["Presentations"],
    }
    return mapping.get(task_name, Exception("Groupset mapping"))


# Get all the group sets -> name : id
def get_group_categories():
    url = "{0}/api/v1/courses/{1}/group_categories".format(CANVAS_URL, CANVAS_COURSE_ID)
    r = requests.get(url, headers={'Authorization': 'Bearer ' + CANVAS_TOKEN})
    return {group["name"]: group["id"] for group in json.loads(r.content)}


# Get assignments -> name : id
def get_assignments():
    url = "{0}/api/v1/courses/{1}/assignments".format(CANVAS_URL, CANVAS_COURSE_ID)
    r = requests.get(url, headers={'Authorization': 'Bearer ' + CANVAS_TOKEN})
    return {assignment["name"]: assignment["id"] for assignment in json.loads(r.content)}


# Get groups in a group set -> name : id
def list_groups(id_group_category):
    url = "{0}/api/v1/group_categories/{1}/groups?per_page=200".format(CANVAS_URL, id_group_category)
    r = requests.get(url, headers={'Authorization': 'Bearer ' + CANVAS_TOKEN})
    return {group["name"]: group["id"] for group in json.loads(r.content)}

# Get groups members -> name : id
def get_group_members(id_group):
    url = "{0}/api/v1/groups/{1}/users".format(CANVAS_URL, id_group)
    r = requests.get(url, headers={'Authorization': 'Bearer ' + CANVAS_TOKEN})
    return {member["name"]: member["id"] for member in json.loads(r.content)}


# Get groups in a group set
def check_group_grading(groups, id_assignment):
    for group in groups:
        members = get_group_members(groups[group])
        for member in members:
            url = "{0}/api/v1/courses/{1}/assignments/{2}/submissions/{3}".format(CANVAS_URL, CANVAS_COURSE_ID,
                                                                                  id_assignment,
                                                                                  members[member])
            r = requests.get(url, headers={'Authorization': 'Bearer ' + CANVAS_TOKEN})
            graded = "graded" == json.loads(r.content)["workflow_state"]
            if not graded:
                print("missing grade for", TASK, "of", group)
                break



# Get sub directories of a given path
def get_sub_directory(path):
    categories = dict()

    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        for category in dirnames:
            categories[category] = {"path": os.path.join(dirpath, category)}
        break

    return categories


# Parse arguments of the script
def parse_args():
    global TASK
    global WEEK
    global DEADLINE
    global CANVAS_TOKEN

    parser = argparse.ArgumentParser()
    parser.add_argument('--task', dest='task', type=str, help='Task name', required=True)
    parser.add_argument('--token', dest='token', type=str, help='Canvas access token', required=True)
    parser.add_argument('--week', dest='week', type=str, help='Week folder (ONLY for presentation/demo)')
    parser.add_argument('--deadline', dest='deadline', type=int, help='Deadline number (NOT for presentation/demo)')

    args = parser.parse_args()
    TASK = args.task
    WEEK = args.week
    DEADLINE = args.deadline
    CANVAS_TOKEN = args.token


# Keep only the groups for a given deadline number
# For each group, we check the readme a look for "task x" if task is not present we keep the group
def filter_deadline_groups(groups, deadline):
    sorted_groups = dict()
    for group in groups:
        f = open(groups[group]["path"] + '/README.md', "r")
        file = f.read().lower()

        if 'task ' not in file:
            sorted_groups[group] = groups[group]
            print("Not sure if the group " + group + " is in for this deadline, checking it anyway\n")
        if 'task ' + deadline in file:
            sorted_groups[group] = groups[group]

    return sorted_groups


def main():
    parse_args()
    canvas_groups_set = get_group_categories()
    canvas_groups_category_id = task_to_set(TASK, canvas_groups_set)
    canvas_groups = list_groups(canvas_groups_category_id)
    canvas_assignment = get_assignments()
    canvas_assignment_id = task_to_set(TASK, canvas_assignment)

    task_sub = get_sub_directory(CONTRIBUTION_PATH + '/' + TASK)

    # Filter github groups according to args
    if WEEK is not None:
        groups = get_sub_directory(task_sub[WEEK]["path"])
        print("Found " + str(len(groups)) + " group(s) for " + TASK + " in " + WEEK)
    elif DEADLINE is not None:
        groups = filter_deadline_groups(task_sub, str(DEADLINE))
        print("Found " + str(len(groups)) + " group(s) for " + TASK + ", deadline " + str(DEADLINE))
    else:
        groups = canvas_groups
        print("Found " + str(len(groups)) + " group(s) for " + TASK)

    # Intersection of canvas groups and github filtered groups
    canvas_groups = {x: canvas_groups[x] for x in canvas_groups if x in groups}

    # Check the grading
    check_group_grading(canvas_groups, canvas_assignment_id)


main()
