#!/usr/bin/python3
"""
0. Gather data from an API
"""

import csv
import requests
import sys

def getrequest():
    url1 = 'https://jsonplaceholder.typicode.com/users/{}'
    url2 = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    users = requests.get(url1.format(sys.argv[1])).json()
    todos = requests.get(url2.format(sys.argv[1])).json()
    with open("{}.csv".format(sys.argv[1]), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            taskwriter.writerow([int(sys.argv[1]), users.get('username'),
                                 task.get('completed'),
                                 task.get('title')])


if __name__ == "__main__":
    getrequest()
