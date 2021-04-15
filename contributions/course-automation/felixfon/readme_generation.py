#!/usr/bin/python
# coding=utf-8

import sys
import os
import re

CONTRIBUTIONS_BASE_PATH = 'contributions/' # path to execute the script from the action
# CONTRIBUTIONS_BASE_PATH = '../../'  # path to execute the script locally


def main():
    """
    - check what readme to generate
    - get metadata for every contribution folder
    :return: nothing
    """
    if len(sys.argv) >= 1:

        contributions_folder = filter(lambda x: os.path.isdir(CONTRIBUTIONS_BASE_PATH + '/' + x),
                                      os.listdir(CONTRIBUTIONS_BASE_PATH))
        for category in contributions_folder:
            build_readme(CONTRIBUTIONS_BASE_PATH + category + '/', category)
    print("job finished")


def build_readme(path, contribution_type):
    """
    For a type of contribution folder, build the readme:
    - get the rules/information of the old readme
    - get information for every contribution
    - update the readme file with the list of the contributions

    :param path: path to the contribution folder with a '/' at the end
    :param contribution_type: e.g. 'demo', 'essay'...
    :return:
    """
    files = os.listdir(path)
    contribution_dir_list = list(filter(lambda f: os.path.isdir(path + f), files))
    # contribution_path_list = list(map(lambda dir: path + dir, contribution_dir_list))

    readme_path = path + 'README.md'
    generated_readme = get_initial_readme_info(readme_path) + '\n\n'
    if contribution_type == 'presentation':
        generated_readme = get_initial_readme_info(readme_path)
        for week in sorted(contribution_dir_list):
            week_path = path + week + '/'
            week_files = os.listdir(week_path)
            week_dirs = list(filter(lambda f: os.path.isdir(week_path + f), week_files))

            generated_readme += '\n- [' + week + '](' + path + week + ')\n'
            for contribution in week_dirs:
                information = get_contribution_information(week_path + contribution, contribution_type)
                if information:
                    generated_readme += '   * ' + information.get("tittle") + " by:\n"
                    for contributor in information.get("contributors"):
                        generated_readme += "      + " + contributor + "\n"
    else:
        for contribution in contribution_dir_list:
            information = get_contribution_information(path + contribution, contribution_type)
            if information:
                generated_readme += '- ' + information.get("tittle") + " by:\n"
                for contributor in information.get("contributors"):
                    generated_readme += "   * " + contributor + "\n"
    with open(readme_path, "w") as readme_file:
        readme_file.write(generated_readme)


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


def get_contribution_information(path, contribution_type):
    """
    From a specific directory, retrieve the information (tittle, names, emails, github...) and format it to a list item
    :param path: the path of contribution folder
    :param contribution_type: e.g. 'demo', 'essay'...
    :return: a dict with formatted markdown information of the tittle and members
    """
    print("analyzing dir: " + path)

    # get the readme of the folder as list of string (per lines)
    readme_path = path + '/README.md'
    try:
        with open(readme_path) as f:
            readme = f.read()
    except IOError:
        print('readme: ' + readme_path + ' not accessible.')
        return ''

    # getting the tittle formatted
    first_line = list(filter(lambda line: line != '', readme.splitlines()))[0].strip()
    tittle = get_tittle(first_line, contribution_type, path.split('/')[-1])

    # getting the member section
    # here we match the part where the contributor(s) are presented.
    pattern = '(#+?\s((Members?)|(Contributors?)|(Authors?)))(((.)|(\s))*?)(#+?\s?\w*?)'
    match = re.search(pattern, readme)

    if match is None:
        members_section = readme
    else:
        members_section = match.group(6)
    # if the readme doesn't correspond, we send the whole readme hoping that we will find the right data on the
    # contributors

    contributors_info = get_contributor_information(members_section)

    # format the contributors to markdown
    first_contributor = ''
    second_contributor = ''
    contributors = []
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
    contributors.append(first_contributor)
    if second_contributor:
        contributors.append(second_contributor)
    return {
        "tittle": tittle,
        "contributors": contributors
    }


def get_tittle(first_line, contribution_type, directory_relative_path):
    """
    From the first line of a repo, get the tittle properly formatted
    :param first_line: the first line of the readme dir
    :param contribution_type: the type of contribution (see dict below)
    :param directory_relative_path: the name of the directory to create the link
    :return: the formatted tittle linked to it
    """
    base_regex = {
        'course-automation': '[cC]ourse [aA]utomation',
        'demo': '([vV]ideo )?[dD]emo',
        'essay': '[eE]ssay',
        'executable-tutorial': '([eE]xecutable )?[tT]utorial',
        'feedback': '[fF][eE][eE][dD][bB][aA][cC][kK]',
        'open-source': '[oO][pP][eE][nN] [sS][oO][uU][rR][cC][eE]',
        'presentation': '[pP][rR][eE][sS][eE][nN][tT][aA][tT][iI][oO][nN]',
    }.get(contribution_type, '')

    # remove surplus #
    tittle = first_line.replace('#', '').strip()

    # remove redundant pre-tittle, e.g. the type of the contribution
    regex_tittle_to_remove = base_regex + '(( [sS]ubmission)|( [pP]roposal))?,?:?'
    tittle = re.sub(regex_tittle_to_remove, '', tittle).strip()
    if tittle == '':
        tittle = contribution_type
    return '[__' + tittle + '__](' + directory_relative_path + ')'


def get_contributor_information(members_text, number_of_contributors=2):
    """
    from the lines in the member section,
    retrieve the name, the email and the github username of each contributors

    :param members_text: the lines of the members section
    :param number_of_contributors: how much contributor should we try to retrieve
    :return: lists of information by contributor
    """
    names = []
    email = []
    github = []
    # kth_user = []

    # get the names (international students so big regex)
    name_pattern = re.compile(
        "([A-ZÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ]{1}"
        "[a-zàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšž]+ [A-ZÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ]{1}"
        "[a-zàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšž]+)")
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
