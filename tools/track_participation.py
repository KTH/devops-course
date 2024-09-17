#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: track_participation.py

import sys
import os
import logging
import json
from github import Github, GithubException
import getopt
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from prettytable import PrettyTable

PRINT_IN_MARKDOWN = False
PUBLISH = False

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_FULLNAME = os.getenv("REPO_FULLNAME")
ISSUE_NUMBER = os.getenv("TRACKER_ISSUE_NUMBER")

config = json.load(open("track_participation_config.json"))

LECTURE_DATES_TO_NUMBER = config['LECTURE_DATES_TO_NUMBER']
LECTURE_DATES_TO_START_TIME = config['LECTURE_DATES_TO_START_TIME']
LECTURE_DURATION_HOURS = config['LECTURE_DURATION_HOURS']
COMMENTING_LEEWAY_HOURS = config['COMMENTING_LEEWAY_HOURS']
LECTURE_TIMEZONE = ZoneInfo(config['LECTURE_TIMEZONE'])

commenting_duration_hours = LECTURE_DURATION_HOURS + COMMENTING_LEEWAY_HOURS

def main():
    handle_args(sys.argv[1:])

    repo, issue = get_repo_and_issue()

    participation = get_participation(issue)

    print_content = ""

    if PRINT_IN_MARKDOWN:
        print_content = get_participation_markdown(participation)
    else:
        print_content = get_participation_text(participation)    

    if PUBLISH:
        update_issue_description(participation, issue)
        print("Updated issue description\n")

    print(print_content)


def get_repo_and_issue():
    """
    Attempts to fetch the GitHub repository and issue using environment variables.
    Exits on failure.
    """
    try:
        github = Github(GITHUB_TOKEN)
        repo = github.get_repo(REPO_FULLNAME)
        issue = repo.get_issue(number=int(ISSUE_NUMBER))
        return repo, issue
    except GithubException as e:
        logging.error(f"GitHub API error: {str(e)}")
        sys.exit(1)


def get_participation(tracking_issue):
    """
    Gets participation by checking each comment on the tracker issue.
    Adds the lecture to the comment author if comment exists. Except if:
        comment is from collaborator
        comment is made outside of allowed time.
    """
    participation = {}

    try:
        collaborators = {collaborator.login for collaborator in tracking_issue.repository.get_collaborators()}
    except GithubException as e:
        logging.error(f"GitHub API error: {str(e)}")
        sys.exit(1)

    for comment in tracking_issue.get_comments():
        author = comment.user.login
        comment_time = comment.created_at.astimezone(LECTURE_TIMEZONE)

        # Ignore collaborators' comments
        if author in collaborators:
            continue

        if is_valid_lecture_time(comment_time):
            lecture_date = comment_time.strftime("%Y-%m-%d")
            if author not in participation:
                participation[author] = {lecture_date}
            else:
                participation[author].add(lecture_date)

    return participation


def is_valid_lecture_time(comment_time):
    """
    Checks if the comment was made on a valid day and time.
    """
    lecture_date_str = comment_time.strftime("%Y-%m-%d")

    if lecture_date_str not in LECTURE_DATES_TO_START_TIME:
        # comment not made on a lecture day
        return False

    lecture_start_hour = LECTURE_DATES_TO_START_TIME[lecture_date_str]

    allowed_period_start = comment_time.replace(hour=lecture_start_hour, minute=0, second=0, microsecond=0)
    allowed_period_end = allowed_period_start + timedelta(hours=commenting_duration_hours)

    # Check if the comment time falls within the valid window
    return allowed_period_start <= comment_time <= allowed_period_end


def update_issue_description(participation, issue):
    """
    Updates the repository issue description in markdown to reflect new participation.
    """
    content = get_participation_markdown(participation)
    try:
        issue.edit(body=content)
    except GithubException as e:
        logging.error(f"GitHub API error: {str(e)}")
        sys.exit(1)


def get_participation_markdown(participation):
    """
    Returns markdown table representation of participation.
    """
    current_time = datetime.now(LECTURE_TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")

    content = f"Here we track active participation in lectures.\n\n"
    content += ("To do this, you record as a comment the question you make to presentations or demos during the "
                "lectures.\n\n")
    content += "Also, provide the title of the presentation/demo.\n\n"
    content += f"### Lecture Participation Stats (Updated on {current_time})\n\n"
    content += "| Index | Student Name | Number of Lectures Attended | Lecture(s) attended |\n"
    content += "|-------|--------------|-------------------|----------------|\n"

    # sort by number of lectures attended
    sorted_participation = sorted(participation.items(), key=lambda item: len(item[1]), reverse=True)

    index = 1
    for author, lectures in sorted_participation:
        lecture_numbers = [f"L{LECTURE_DATES_TO_NUMBER[lecture]}" for lecture in sorted(lectures)]
        lectures_list = " ".join(map(str, lecture_numbers))
        total_lectures = len(lectures)
        content += f"| {index} | {author} | {total_lectures} | {lectures_list} |\n"
        index += 1

    return content


def get_participation_text(participation):
    """
    Returns plaintext table representation of participation.
    """
    current_time = datetime.now(LECTURE_TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")

    table = PrettyTable()
    table.field_names = ["Index", "Student Name", "Number of Lectures Attended", "Lecture(s) attended"]

    # sort by number of lectures attended
    sorted_participation = sorted(participation.items(), key=lambda item: len(item[1]), reverse=True)

    index = 1
    for author, lectures in sorted_participation:
        lecture_numbers = [f"L{LECTURE_DATES_TO_NUMBER[lecture]}" for lecture in sorted(lectures)]
        lectures_list = " ".join(map(str, lecture_numbers))
        total_lectures = len(lectures)
        table.add_row([index, author, total_lectures, lectures_list])
        index += 1

    return_str = f"Lecture Participation Stats (Updated on {current_time})\n\n"
    return_str += table.get_string()

    return return_str


def handle_args(argv):
    global PRINT_IN_MARKDOWN
    global PUBLISH

    try:
        opts, args = getopt.getopt(argv, "hm", ["help", "printMarkdown", "publish"])
    except getopt.GetoptError as error:
        logging.error(error)
        print_help_info()
        sys.exit(2)

    for opt, _ in opts:
        if opt == "--help":
            print_help_info()
            sys.exit()
        elif opt == "--printMarkdown":
            PRINT_IN_MARKDOWN = True
        elif opt == "--publish":
            PUBLISH = True


def print_help_info():
    print('')
    print('DD2482 Student Lecture Participation Tracker Tool')
    print('')
    print('optional:')
    print('    --printMarkdown Print participation in markdown syntax')
    print('    --publish              Update the participation tracker issue')
    print('')
    print('track_participation.py --help to display this help info')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if not GITHUB_TOKEN or not REPO_FULLNAME or not ISSUE_NUMBER:
        logging.error("Required environment variables (GITHUB_TOKEN, REPO_FULLNAME, ISSUE_NUMBER) are missing")
        sys.exit(1)
    main()
