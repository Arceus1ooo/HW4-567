import unittest

from RepoLister import countCommits

class TestCommitCounter(unittest.TestCase):

    def test_HW2567(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW2-567'), 12)

    def test_HW1567(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW1-567'), 6)

    def test_helloworld(self):
        self.assertEqual(countCommits('Arceus1ooo', 'helloworld'), 4)
    def test_Exchange4Students(self):
        self.assertEqual(countCommits('Arceus1ooo', 'Exchange4Students'), 96)
    def test_HW5345(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW5-345'), 4)
    def Test_DungeonKnight(self):
        self.assertEqual(countCommits('Arceus1ooo', 'Dungeon-Knight'), 134)
    def test_HW4345(self):
        self.assertEqual(countCommits('Arceus1ooo', 'HW4-345'), 490)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()