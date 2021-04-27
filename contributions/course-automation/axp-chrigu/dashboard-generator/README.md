# Dashboard generator

A GitHub action to generate a dashboard for the repository of the course DD2482 (DevOps). The action categorize submissions by year, type of task, and technology keywords.

## Output

`dashboard` - The generated dashboard markdown, in string form.

The generated sections are described below.

### Submissions per year

A table that shows how many submissions are made per year of the course.

### Year submission

These sections shows all of the submissions done for each year, categorized into the category of the submissions.

### Keywords

This section shows a summary of technology keywords used in the description of the submission.

## Usage

```yaml
name: Generate Dashboard
on: push

jobs:
    generate-dashboard:
        name: Generate dashboard
        runs-on: ubuntu-20.04
        steps:
            - uses: actions/checkout@v2.3.4
            - name: Generate dashboard
              uses: ./contributions/course-automation/axp-chrigu/dashboard-generator/
              id: dashboard
            - name: Push new dashboard
              id: push
              run: |
                  echo "${{ steps.dashboard.outputs.dashboard }}" > dashboard.md
                  if [ -z "$(git status --porcelain)" ]; then
                    echo "::set-output name=did_push::false"
                  else
                    git config --global user.name 'Dashboard bot'
                    git config --global user.email 'dashboard-bot-dd2482@users.noreply.github.com'
                    git add ./dashboard.md
                    git commit -m "Generated dashboard"
                    git push
                    echo "::set-output name=did_push::true"
                  fi
```

## Contributors

Axel Pettersson - [Ackuq](https://github.com/Ackuq)
Christopher Gustafson - [ChristopherGustafson](https://github.com/ChristopherGustafson)
