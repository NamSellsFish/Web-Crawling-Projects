# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests
import datetime

# Start working
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
    'name': 'TestBoard',
    'key': 'bb5b01bc6d8e5986963a43496e5fc6c9',
    'token': '8853696c580eb7413a90e6d2933121722e165caba06e6a5c83987ad510bef380'
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
        'key': 'bb5b01bc6d8e5986963a43496e5fc6c9',
        'token': '8853696c580eb7413a90e6d2933121722e165caba06e6a5c83987ad510bef380'
    }
    list = ses.request(
        "POST",
        url2,
        params=query
    )
    ListOfID.append(list.json()["id"])

# Create cards
for i in range(1, 13):
    query = {
        'name': f'Bài {i}',
        'idList': f'{ListOfID[2] if i % 2 != 0 else ListOfID[1]}',
        'key': 'bb5b01bc6d8e5986963a43496e5fc6c9',
        'token': '8853696c580eb7413a90e6d2933121722e165caba06e6a5c83987ad510bef380'
    }
    card = ses.request(
        "POST",
        url3,
        params=query
    )
