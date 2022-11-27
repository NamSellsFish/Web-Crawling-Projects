# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import argparse
import os
from typing import List, Tuple

import requests
import datetime

# Get args
argp = argparse.ArgumentParser()
argp.add_argument("key", help="Trello key")
argp.add_argument("key", help="Trello token")
argp.add_argument("course_code", help="e.g: HN2006")
argp.add_argument("start_date", help="e.g 2020/06/25")
args = argp.parse_args()
start = datetime.datetime.strptime(args.start_date, "%Y/%m/%d")
course_code = args.course_code.upper()
location = "Hà Nội" if course_code.startswith("HN") else "Tp Hồ Chí Minh"
key = args.key
token = args.token

# Start working #
ses = requests.session()
url1 = "https://api.trello.com/1/boards/"
url2 = "https://api.trello.com/1/lists"
url3 = "https://api.trello.com/1/cards"
ListOfID = []
headers = {
    "Accept": "application/json"
}

# Create board
query = {
    'name': "Học Python {} PYMI.vn {} timetable".format(
        location, course_code
    ),
    'key': key,
    'token': token
}

board = ses.request(
    "POST",
    url1,
    params=query
)
ListOfID.append(board.json()["id"])

# Create lists
for i in range(5, 2, -2):
    query = {
        'name': 'Thứ {}'.format(i),
        'idBoard': '{}'.format(ListOfID[0]),
        'key': key,
        'token': token

    }
    list = ses.request(
        "POST",
        url2,
        params=query
    )
    ListOfID.append(list.json()["id"])


# Create cards
    def days_for_class(
            start: datetime.datetime, n=12
    ) -> List[Tuple[str, int]]:
        days: List[Tuple[str, int]] = []
        count = 1
        day = start
        while count <= n:
            # tuesday / thursday
            if day.isoweekday() in [2, 4]:
                days.append((day.strftime("%Y/%m/%d"), day.isoweekday()))
                count = count + 1
            day = day + datetime.timedelta(days=1)

        return days

for i, (date, dow) in enumerate(days_for_class(start), start=1):
    query = {
        'name': f'Bài {i}',
        'idList': f'{ListOfID[2] if i % 2 != 0 else ListOfID[1]}',
        'due': date,
        'key': key,
        'token': token
    }
    card = ses.request(
        "POST",
        url3,
        params=query
    )
