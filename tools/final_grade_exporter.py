#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: final_grade_exporter.py
import csv
import json
import argparse, requests

CANVAS_TOKEN = ''
EXPORT_PATH = ''
FIELDS = ''
CANVAS_URL = "https://canvas.kth.se"
CANVAS_COURSE_ID = 31421


# Get list of students {canvas_id, name, kth_id}
def get_students():
    url = "{0}/api/v1/courses/{1}/users?per_page=200&enrollment_type[]=student".format(CANVAS_URL, CANVAS_COURSE_ID)
    r = requests.get(url, headers={'Authorization': 'Bearer ' + CANVAS_TOKEN})
    return [{"canvas_id": user["id"], "name": user["name"], "kth_id": user["email"].split("@")[0]} for user in
            json.loads(r.content)]


# Get graded submission with complete grade for a canvas user, list of assignments name
def get_completed_submissions(canvas_id):
    url = "{0}/api/v1/courses/{1}/students/submissions?workflow_state=graded&student_ids[]={2}&include[]=assignment".format(
        CANVAS_URL,
        CANVAS_COURSE_ID,
        canvas_id)
    r = requests.get(url, headers={'Authorization': 'Bearer ' + CANVAS_TOKEN})
    return [submission["assignment"]["name"] for submission in json.loads(r.content) if
            submission["grade"] == "complete"]


# Compute the grade according to the number of completed assignments
# Ignore feedback for grade E
def compute_grade(completed_assignments):
    nb_assignments = len(completed_assignments)

    if nb_assignments >= 5:
        return "A"
    elif nb_assignments == 4:
        return "C"
    elif nb_assignments == 3 and "Feedback" not in completed_assignments:
        return "E"
    else:
        return "F"


# Parse arguments of the script
def parse_args():
    global CANVAS_TOKEN
    global EXPORT_PATH
    global FIELDS
    parser = argparse.ArgumentParser()

    parser.add_argument('--token', dest='token', type=str, help='Canvas access token', required=True)
    parser.add_argument('--fields', dest='fields', type=str, nargs='+', help='Fiedls to export',
                        default=["name", "kth_id", "grade"])
    parser.add_argument('--export', dest='export_path', type=str, help='Path to write csv file', required=False,
                        default='')

    args = parser.parse_args()
    CANVAS_TOKEN = args.token
    EXPORT_PATH = args.export_path
    FIELDS = args.fields


def main():
    parse_args()

    students = get_students()

    # Get completed assignments for each students and compute the grade
    for i in range(0, len(students)):
        completed = get_completed_submissions(students[i]["canvas_id"])
        students[i]["completed"] = completed
        students[i]["grade"] = compute_grade(completed)
        print("{0},{1},{2}".format(students[i]["name"], students[i]["kth_id"], students[i]["grade"]))

    if EXPORT_PATH != '':
        # Write the result to csv file
        with open(EXPORT_PATH, mode='w') as grade_file:
            grade_writer = csv.DictWriter(grade_file, delimiter=',', fieldnames=FIELDS,
                                          extrasaction='ignore')
            grade_writer.writeheader()
            grade_writer.writerows(students)


main()
