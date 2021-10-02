import json
import requests
from pprint import pprint

def countCommits(repo):
    counter = 0
    for commit in repo:
        counter += 1
    return counter

def getRepoNames(request):
    names = []
    for repo in request:
        for header in repo:
            if header == 'name':
                names.append(repo[header])
    return names

def displayRepos(user):
    repoRequest = requests.get(f'https://api.github.com/users/{user}/repos').json()
    repoNames = getRepoNames(repoRequest)
    for name in repoNames:
        if name == 'HW4-345':
            commitRequest = requests.get(f'https://api.github.com/repos/{user}/{name}/commits').json()
            commits = countCommits(commitRequest)
            counter = 0
            for body in commitRequest:
                if body['commit'] is not None:
                    counter += 1
                    print(body['commit']['author']['date'])
               
            print(counter)
            print(f'Repo: {name}, Number of commits: {commits}')

displayRepos('Arceus1ooo')