#!/usr/bin/env bash

#TODO there is an argument to be made for keeping this script in the root of the directory (so that the invocation command is just ./mpr, not ./scripts/mpr

help () {
  echo "Helpful info for you :)"
  echo "_______________________"
  echo "This command is designed to be run on your local machine from a forked copy of the KTH devops course repository."
  echo "It will push your local branch to its remote counterpart and open a PR in the devops repo."
  echo "Devops repo URL: https://github.com/KTH/devops-course"
  echo "The command prompts you for a PR title, which is auto-added to the PR which will be opened."
  echo "_______________________"
  echo "I recommend that you add an alias to your shell rc file like this, so you can run mpr from anywhere:"
  echo "alias mpr=/Users/{username}/{path-to-forked-repository}/scripts/mpr"
  echo "_______________________"
  echo "This script was initially written for use in a bash or zsh shell on macOS. It will open the PR in a new Chrome tab."
  echo "Please feel free to address issues in future PRs!"
}

make_pr (){
  # Get branch to make PR from
  CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

  echo "Pushing local branch ${CURRENT_BRANCH} to remote."
  git push
  echo

  BASE_GITHUB_URL="https://github.com/KTH/devops-course/compare/"

  # Infer github username from remote url
  GH_REMOTE_ORIGIN=$(git config remote.origin.url)
  URL_WITHOUT_SUFFIX="{$GH_REMOTE_ORIGIN%.*}"
  REPO_NAME="$(basename "${URL_WITHOUT_SUFFIX}")"
  GH_USERNAME="$(basename "${URL_WITHOUT_SUFFIX%/${REPO_NAME}}")"

  # User confirmation of GH Username
  read -r "USER?Git Username (enter for inferred username ${GH_USERNAME}):"

  # Get current year's main branch
  CURRENT_YEAR=$(date +"%Y")

  # Get desired title as CLI input
  echo
  echo "What should the title of this PR be? (Something like \"Presentation Proposal: Optimizing Test Suite Runtimes in Large Software Applications\")"
  read -r "TITLE?Title: "

  # Construct PR URL
  PR_URL="${BASE_GITHUB_URL}${CURRENT_YEAR}...${GH_USERNAME}:${CURRENT_BRANCH}?expand=1"
  if [ "$TITLE" ]
  then
    echo "Using title ${TITLE}"
    PR_URL="${PR_URL}&title=${TITLE}"
  else
    echo "No title given - you can add one in the web UI"
  fi

  echo
  echo "Opening PR..."
  open "$PR_URL"

  exit 0
}

while getopts ":h" option; do
   case $option in
      h) # display Help
         help
         exit 0;;
      \?) # invalid option
         echo "Error: Invalid option"
         exit 1;;
   esac
done

echo "Creating a pull request..."
echo

# Use pushd to change into the root directory of the project
pushd $(git rev-parse --show-toplevel) > /dev/null || exit 0
make_pr
popd > /dev/null || exit 0
