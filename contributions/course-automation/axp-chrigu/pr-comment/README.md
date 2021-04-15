# PR Comment action

A GitHub action to comment on a PR.

## Input

`message` (required) - The message that should be included in the comment.

`GITHUB_TOKEN` (required) - The token used to authenticate against GitHub. If you want to use the default GitHub actions token you can access it using `${{ secrets.GITHUB_TOKEN }}`.

## Usage

```yaml
name: Comment on PR
on: pull_request

jobs:
  make-comment:
    name: Comment
      runs-on: ubuntu-20.04
      steps:
        - uses: ./contributions/course-automation/axp-chrigu/pr-comment/
          with:
            message: 'This is a comment'
            GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Contributors

Axel Pettersson - [Ackuq](https://github.com/Ackuq)
Christopher Gustafson - [ChristopherGustafson](https://github.com/ChristopherGustafson)
