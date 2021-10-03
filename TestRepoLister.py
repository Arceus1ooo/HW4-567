import unittest

from RepoLister import countCommits

class TestCommitCounter(unittest.TestCase):
    def Test_HW2567(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW2-567'), 12, "There are 12 commits in HW2-567")
    def Test_HW1567(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW1-567'), 6)
    def Test_helloworld(self):
        self.assertEqual(countCommits('Arceus1ooo', 'helloworld'), 4)
    def Test_Exchange4Students(self):
        self.assertEqual(countCommits('Arceus1ooo', 'Exchange4Students'), 96)
    def Test_HW5345(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW5-345'), 4)
    def Test_DungeonKnight(self):
        self.assertEqual(countCommits('Arceus1ooo', 'Dungeon-Knight'), 134)
    def Test_HW4345(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW4-345'), 490)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()