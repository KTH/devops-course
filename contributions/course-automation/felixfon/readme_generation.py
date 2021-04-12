#!/usr/bin/python
# coding=utf-8

import sys
import os
from functools import reduce
import re

CONTRIBUTIONS_BASE_PATH = '../../'

def main():
    """
    - todo
    - check what readme to generate
    - get metadata for every contribution folder
    :return: nothing
    """
    if len(sys.argv) >= 1:

        contributions_folder = filter(lambda x: os.path.isdir(CONTRIBUTIONS_BASE_PATH + '/' + x), os.listdir(CONTRIBUTIONS_BASE_PATH))
        for category in contributions_folder:
            if not category == 'presentation':
                build_readme(CONTRIBUTIONS_BASE_PATH + category + '/')


def build_readme(path):
    """
    For a contribution folder, build the readme:
    - get the rules/information of the old readme
    - get information for every contribution
    - update the readme file with the list of the contributions
    :param path:
    :return:
    """
    files = os.listdir(path)
    contribution_dir_list =  filter(lambda f: os.path.isdir(path + f), files)
    contribution_path_list = list(map(lambda dir: path + dir, contribution_dir_list))
    readme_path = path + 'README.md'

    # a
    generated_readme = reduce((lambda readme, contribution: readme + '\n' + get_contribution_information(contribution)),
                              contribution_path_list,
                              get_initial_readme_info(readme_path))
    print(generated_readme)


def get_initial_readme_info(readme_path):
    """
    Get the initial lines of a readme, ignoring the list of contributions generated previously
    :param readme_path: the path of the readme
    :return: the initial lines of a the readme as string separated by '\n'
    """
    with open(readme_path) as f:
        base_readme = ''
        lines = f.read().splitlines()
        for l in lines:
            line = l.strip()
            if (line == '## List of contributions'):
                break
            base_readme += line + '\n'
        return base_readme + '## List of contributions'


def get_contribution_information(path):
    """

    :param path: the path of contribution folder
    :return: list of information
    """
    print("aaaa: " + path)

    # get the readme of the folder as list of string (per lines)
    # get the contribution title
    # get the members information
    # analyse the members part to retrieve names/mails/github...
    readme_path = path + '/README.md'
    try:
        with open(readme_path) as f:
            readme = f.read()
    except: # readme not found or not readable
        return ''
    # getting the tittle
    first_line = readme.splitlines()[0]
    tittle = first_line.replace('#', '').strip()
    # getting the member section
    try:
        # here we match the part where the contributor(s) are presented.
        pattern = '(#+?\s((Members?)|(Contributors?)|(Authors?)))(((.)|(\s))*?)(#+?\s\w*?)'
        match = re.search(pattern, readme)
        members_section = match.group(6)
    except:
        # if the readme doesn't correspond, we send the whole readme hoping that we will find the right data on the
        # contributors
        members_section = readme
    contributors_info = get_contributor_information(members_section)

    # building of a list item
    first_contributor = ''
    second_contributor = ''
    if contributors_info["names"]:
        first_contributor += contributors_info["names"][0]
        if len(contributors_info["names"]) > 1:
            second_contributor += contributors_info["names"][1]
    if contributors_info["emails"]:
        if len(first_contributor) > 0:
            first_contributor += ', '
        first_contributor += 'email: ' + contributors_info["emails"][0]
        if len(contributors_info["emails"]) > 1:
            if len(second_contributor) > 0:
                second_contributor += ', '
            second_contributor += 'email: ' + contributors_info["emails"][1]

    if contributors_info["githubs"]:
        if len(first_contributor) > 0:
            first_contributor += ', '
        first_contributor += 'github: ' + contributors_info["githubs"][0]
        if len(contributors_info["githubs"]) > 1:
            if len(second_contributor) > 0:
                second_contributor += ', '
            second_contributor += 'github: ' + contributors_info["githubs"][1]
    base = '- __' + tittle + '__ by ' + first_contributor
    if second_contributor:
        return base + ' and ' + second_contributor
    return base


def get_contributor_information(members_text, number_of_contributors=2):
    """
    from the lines in the member section,
    retrieve the name, the email and the github username of each contributors
    :param member_lines: the lines of the members section
    :return: lists of information by contributor
    """
    names = []
    email = []
    github = []
    # kth_user = []

    name_pattern = re.compile("([A-ZÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ]{1}[a-zàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšž]+ [A-ZÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ]{1}[a-zàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšž]+)")
    email_pattern = re.compile("([\w\.-]+@[\w\.-]+\.[\w]+)")
    github_pattern = re.compile("(\[[a-zA-Z]+\]\(https://github\.com/[a-z]+/?\))")

    names = name_pattern.findall(members_text)[:number_of_contributors]

    emails = email_pattern.findall(members_text)[:number_of_contributors]

    githubs = github_pattern.findall(members_text)[:number_of_contributors]

    if not githubs:
        github_pattern2 = re.compile("(https://github\.com/[a-z]+/?)")
        githubs = github_pattern2.findall(members_text)[:number_of_contributors]
        if not githubs:
            github_pattern3 = re.compile("Github: ([a-z]+/?)")
            githubs = github_pattern3.findall(members_text)[:number_of_contributors]

    return {
        "names": names,
        "emails": emails,
        "githubs": githubs
    }

main()
