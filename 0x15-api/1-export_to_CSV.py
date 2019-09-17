#!/usr/bin/python3
"""
0. Gather data from an API
"""
import requests
import sys

text1 = "Employee {} is done with tasks({}/{}):"
url1 = 'https://jsonplaceholder.typicode.com/users/{}'
url2 = 'https://jsonplaceholder.typicode.com/todos'
def getrequest():
    users = requests.get(url1.format(sys.argv[1]))
    names = users.json().get('name')
    todos = requests.get(url2)
    todos = todos.json()
    comp = 0
    titles = []
    total = 0
    for todo in todos:
        if todo['userId'] == int(sys.argv[1]):
            if todo['completed'] is True:
                comp += 1
                titles.append(todo['title'])
            total += 1
    print(text1.format(names, comp, total))
    for title in titles:
        print('\t ', end="")
        print(title)


if __name__ == "__main__":
    getrequest()
