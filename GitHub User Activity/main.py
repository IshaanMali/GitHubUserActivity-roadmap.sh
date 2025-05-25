import json
import requests

username = input("Type in the username to get the user's recent GitHub activity: ")
response = requests.get(f"https://api.github.com/users/{username}/events").text
lst = json.loads(response)
for event in lst:
    if event["type"] == "PushEvent":
        repo = event["repo"]["name"]
        no_of_commits = 0
        for commit in event["payload"]["commits"]:
            no_of_commits+=1
        if no_of_commits == 1:
            print(f"Pushed 1 commit to {repo}")
        else:
            print(f"Pushed {no_of_commits} commits to {repo}")
    elif event["type"] == "CreateEvent":
        repo = event["repo"]["name"]
        print(f"Created repository - {repo}")
    elif event["type"] == "IssuesEvent":
        issue = event["payload"]["issue"]["title"]
        repo = event["repo"]["name"]
        action = event["payload"]["action"]
        print(f"{action.capitalize()} an issue in {repo} titled - {issue}")
    elif event["type"] == "IssueCommentEvent":
        comment = event["payload"]["comment"]["body"]
        repo = event["repo"]["name"]
        action = event["payload"]["action"]
        print(f"{action.capitalize()} a comment in {repo} - {comment}")
    elif event["type"] == "WatchEvent":
        repo = event["repo"]["name"]
        print(f"Starred {repo}")
    elif event["type"] == "ForkEvent":
        repo = event["repo"]["name"]
        print(f"Forked {repo}")