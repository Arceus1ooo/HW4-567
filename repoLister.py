import json
import requests
from pprint import pprint
import unittest

class TestCommitCounter(unittest.TestCase):

    def test_HW2567(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW2-567'), 12)
    def test_HW1567(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW1-567'), 6)
    def test_helloworld(self):
        self.assertEqual(countCommits('Arceus1ooo', 'helloworld'), 4)
    def test_HW3(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW3'), 3)
    def test_HW5345(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW5-345'), 4)
    def test_DesignPatternLab(self):
        self.assertEqual(countCommits('Arceus1ooo', 'DesignPatternLab'), 2)
    def test_Complexity(self):
        self.assertEqual(countCommits('Arceus1ooo', 'Complexity'), 2)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

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
    for name in repoNames:
        commits = countCommits(user, name)
        print(f'Repo: {name}, Number of commits: {commits}')