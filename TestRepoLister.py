import unittest

#from RepoLister import countCommits, getRepoNames
import RepoLister
from unittest import mock

class TestCommitCounter(unittest.TestCase):

    @mock.patch("RepoLister.getRepoNames")
    def test_Arceus1ooo(self, mock_repoNames):
        mock_repoNames.return_value.names = ['Complexity', 'DesignPatternLab', 'Dungeon-Knight',
        'Exchange4Students', 'helloworld', 'HW1-567', 'HW2-567', 'HW3', 'HW4', 'HW4-345', 'HW4-567',
        'HW5-345', 'HW5-567', 'Node.js-Application-Lab', 'SSW345TeamProject', 'test-HW4-345']
        response = RepoLister.getRepoNames('Arceus1ooo')
        self.assertNotEqual(response.names, [])

    @mock.patch("RepoLister.getRepoNames")
    def test_Repo1(self, mock_repoNames):
        mock_repoNames.return_value.names = ['Complexity', 'DesignPatternLab', 'Dungeon-Knight',
        'Exchange4Students', 'helloworld', 'HW1-567', 'HW2-567', 'HW3', 'HW4', 'HW4-345', 'HW4-567',
        'HW5-345', 'HW5-567', 'Node.js-Application-Lab', 'SSW345TeamProject', 'test-HW4-345']
        response = RepoLister.getRepoNames('Arceus1ooo')
        self.assertIn('HW4-567', response.names)

    @mock.patch("RepoLister.getRepoNames")
    def test_Repo2(self, mock_repoNames):
        mock_repoNames.return_value.names = ['Complexity', 'DesignPatternLab', 'Dungeon-Knight',
        'Exchange4Students', 'helloworld', 'HW1-567', 'HW2-567', 'HW3', 'HW4', 'HW4-345', 'HW4-567',
        'HW5-345', 'HW5-567', 'Node.js-Application-Lab', 'SSW345TeamProject', 'test-HW4-345']
        response = RepoLister.getRepoNames('Arceus1ooo')
        self.assertIn('Exchange4Students', response.names)

    @mock.patch("RepoLister.getRepoNames")
    def test_Repo3(self, mock_repoNames):
        mock_repoNames.return_value.names = ['Complexity', 'DesignPatternLab', 'Dungeon-Knight',
        'Exchange4Students', 'helloworld', 'HW1-567', 'HW2-567', 'HW3', 'HW4', 'HW4-345', 'HW4-567',
        'HW5-345', 'HW5-567', 'Node.js-Application-Lab', 'SSW345TeamProject', 'test-HW4-345']
        response = RepoLister.getRepoNames('Arceus1ooo')
        self.assertIn('Dungeon-Knight', response.names)

    @mock.patch("RepoLister.countCommits")
    def test_HW2567(self, mock_countCommits):
        mock_countCommits.return_value.commits = 12
        response = RepoLister.countCommits('Arceus1ooo', 'HW2-567')
        self.assertEqual(response.commits, 12)

    @mock.patch("RepoLister.countCommits")
    def test_HW1567(self, mock_countCommits):
        mock_countCommits.return_value.commits = 6
        response = RepoLister.countCommits('Arceus1ooo', 'HW1-567')
        self.assertEqual(response.commits, 6)

    @mock.patch("RepoLister.countCommits")
    def test_helloworld(self, mock_countCommits):
        mock_countCommits.return_value.commits = 4
        response = RepoLister.countCommits('Arceus1ooo', 'helloworld')
        self.assertEqual(response.commits, 4)

    @mock.patch("RepoLister.countCommits")
    def test_HW3(self, mock_countCommits):
        mock_countCommits.return_value.commits = 3
        response = RepoLister.countCommits('Arceus1ooo', 'HW3')
        self.assertEqual(response.commits, 3)

    @mock.patch("RepoLister.countCommits")
    def test_HW5345(self, mock_countCommits):
        mock_countCommits.return_value.commits = 4
        response = RepoLister.countCommits('Arceus1ooo', 'HW5-345')
        self.assertEqual(response.commits, 4)

    @mock.patch("RepoLister.countCommits")
    def test_DesignPatternLab(self, mock_countCommits):
        mock_countCommits.return_value.commits = 2
        response = RepoLister.countCommits('Arceus1ooo', 'DesignPatternLab')
        self.assertEqual(response.commits, 2)

    @mock.patch("RepoLister.countCommits")
    def test_Complexity(self, mock_countCommits):
        mock_countCommits.return_value.commits = 2
        response = RepoLister.countCommits('Arceus1ooo', 'Complexity')
        self.assertEqual(response.commits, 2)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
    @mock.patch("RepoLister.getRepoNames")
    def mock_getRepoNames(mock_repoNames):
        mock_repoNames.return_value.ok = True
        response = RepoLister.getRepoNames('Arceus1ooo')
        print(response)
        print(mock_repoNames.return_value)

    mock_getRepoNames()