# Tools

## missing_grade.py
This script is used to list the group who have not received a grade on canvas.

### Requirements 

- Python 3
- External modules
  - argparse
  - requests

### Usage

`python missing_grade.py --task executable-tutorial --deadline 1 --token 8779~...`

`python missing_grade.py --task presentation --week week2-testing-and-CI --token 88779~...`

| Option | Usage | Required | Note |
|---|---|---|---|
|--task| Task name you want to check  | :heavy_check_mark:||
|--token| Canvas access token generated on [on your profile](https://canvas.kth.se/profile/settings) | :heavy_check_mark:||
|--week| Filter the by week folder |:x:| ONLY for presentation or demo |
|--deadline| Filter the by task deadline |:x:| NOT for presentation or demo|


`--week` and `--deadline` are optional, if you don't give them, you'll get all non graded groups for this task


## stat_submission.py

### Requirements 
...

### Usage
...