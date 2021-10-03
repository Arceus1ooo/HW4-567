import json
import requests
from pprint import pprint

def countCommits(user, repoName):
    commitRequest = requests.get(f'https://api.github.com/repos/{user}/{repoName}/commits').json()
    counter = 0
    for commit in commitRequest:
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
    print(repoRequest)
    for name in repoNames:
        commits = countCommits(user, name)
        print(f'Repo: {name}, Number of commits: {commits}')

displayRepos('Arceus1ooo')