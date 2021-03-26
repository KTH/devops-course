import os, json
import datetime
from dateutil import dateutil

MINWORDREQ = 10 #actual requirement is 500 words
REMARKWORDREQ = 20 # requirement for remarkable feedback is at least 1000 words
DEADLINE = datetime.datetime(2021,4,26,00,00).isoformat() # the feedback comment should be sent 4 days before the deadline of the task
time_created = datetime.datetime.strptime("2021-03-25T17:39:15Z", "%Y-%m-%dT%H:%M:%S%z")


def main():
    print(DEADLINE)
    res = DEADLINE - time_created
    print(res)

#def create_comment_text():



#def check_requirements(word_count, time_created):


if __name__ == "__main__":
    main()