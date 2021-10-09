import unittest

from RepoLister import countCommits, getRepoNames

class TestCommitCounter(unittest.TestCase):

    def test_Arceus1ooo(self):
        self.assertNotEqual(getRepoNames('Arceus1ooo'), [])
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