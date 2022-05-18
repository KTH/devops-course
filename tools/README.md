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

## final_grade_exporter.py
This script is used to grade each student according to the number of task completed

### Requirements 

- Python 3
- External modules
  - argparse
  - requests

### Usage

`python3 final_grade_exporter.py --token 88779~...`

`python3 final_grade_exporter.py --token 88779~... --export grade.csv`

`python3 final_grade_exporter.py --token 88779~... --export grade.csv --fields kth_id grade`

| Option | Usage | Required | Default|
|---|---|---|---|
|--token| Canvas access token generated on [on your profile](https://canvas.kth.se/profile/settings) | :heavy_check_mark:||
|--export| Path where to write the csv file  |:x:| No writing  |
|--fields| Specify fields to write, *canvas_id name kth_id completed grade*  |:x:| name kth_id grade|


## stat_submission.py

### Requirements 
...

### Usage
...