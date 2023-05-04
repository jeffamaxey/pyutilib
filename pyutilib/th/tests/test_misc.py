import os
from os.path import abspath, dirname
currdir = dirname(abspath(__file__)) + os.sep

import pyutilib.th as unittest


class Tester(unittest.TestCase):

    def test1(self):
        self.assertFileEqualsBaseline(
            f'{currdir}file1.txt', f'{currdir}file1.txt', delete=False
        )
        self.assertFileEqualsBaseline(
            f'{currdir}file2.txt', f'{currdir}file2.txt', delete=False
        )

    @unittest.expectedFailure
    def test2(self):
        self.assertFileEqualsBaseline(
            f'{currdir}file1.txt', f'{currdir}file2.txt', delete=False
        )

    def test3(self):
        self.assertFileEqualsBaseline(
            f'{currdir}file1.txt', f'{currdir}file1.zip', delete=False
        )
        self.assertFileEqualsBaseline(
            f'{currdir}file1.zip', f'{currdir}file1.txt', delete=False
        )
        self.assertFileEqualsBaseline(
            f'{currdir}file1.zip', f'{currdir}file1.zip', delete=False
        )
        self.assertFileEqualsBaseline(
            f'{currdir}file2.txt', f'{currdir}file2.zip', delete=False
        )
        self.assertFileEqualsBaseline(
            f'{currdir}file2.zip', f'{currdir}file2.txt', delete=False
        )
        self.assertFileEqualsBaseline(
            f'{currdir}file2.zip', f'{currdir}file2.zip', delete=False
        )

    def test3gz(self):
        self.assertFileEqualsBaseline(
            f'{currdir}file1.txt', f'{currdir}file1.txt.gz', delete=False
        )
        self.assertFileEqualsBaseline(
            f'{currdir}file1.txt.gz', f'{currdir}file1.txt', delete=False
        )
        self.assertFileEqualsBaseline(
            f'{currdir}file1.txt.gz', f'{currdir}file1.txt.gz', delete=False
        )
        self.assertFileEqualsBaseline(
            f'{currdir}file2.txt', f'{currdir}file2.txt.gz', delete=False
        )
        self.assertFileEqualsBaseline(
            f'{currdir}file2.txt.gz', f'{currdir}file2.txt', delete=False
        )
        self.assertFileEqualsBaseline(
            f'{currdir}file2.txt.gz', f'{currdir}file2.txt.gz', delete=False
        )

    @unittest.expectedFailure
    def test4(self):
        self.assertFileEqualsBaseline(
            f'{currdir}file1.txt', f'{currdir}file3.zip', delete=False
        )

    @unittest.expectedFailure
    def test5(self):
        self.assertFileEqualsBaseline(
            f'{currdir}file3.zip', f'{currdir}file1.txt', delete=False
        )

    @unittest.expectedFailure
    def test6(self):
        self.assertFileEqualsBaseline(
            f'{currdir}file1.zip', f'{currdir}file3.txt', delete=False
        )

    @unittest.expectedFailure
    def test7(self):
        self.assertFileEqualsBaseline(
            f'{currdir}file3.zip', f'{currdir}file3.zip', delete=False
        )

    @unittest.expectedFailure
    def test8(self):
        self.assertFileEqualsBaseline(
            f'{currdir}file1.zip', f'{currdir}file2.zip', delete=False
        )

    @unittest.expectedFailure
    def test8gz(self):
        self.assertFileEqualsBaseline(
            f'{currdir}file1.txt.gz', f'{currdir}file2.txt.gz', delete=False
        )



class TesterL(unittest.TestCase):

    def test1(self):
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.txt', f'{currdir}file1.txt', delete=False
        )
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file2.txt', f'{currdir}file2.txt', delete=False
        )

    @unittest.expectedFailure
    def test2(self):
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.txt', f'{currdir}file2.txt', delete=False
        )

    def test3(self):
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.txt', f'{currdir}file1.zip', delete=False
        )
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.zip', f'{currdir}file1.txt', delete=False
        )
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.zip', f'{currdir}file1.zip', delete=False
        )
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file2.txt', f'{currdir}file2.zip', delete=False
        )
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file2.zip', f'{currdir}file2.txt', delete=False
        )
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file2.zip', f'{currdir}file2.zip', delete=False
        )

    def test3gz(self):
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.txt', f'{currdir}file1.txt.gz', delete=False
        )
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.txt.gz', f'{currdir}file1.txt', delete=False
        )
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.txt.gz', f'{currdir}file1.txt.gz', delete=False
        )
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file2.txt', f'{currdir}file2.txt.gz', delete=False
        )
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file2.txt.gz', f'{currdir}file2.txt', delete=False
        )
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file2.txt.gz', f'{currdir}file2.txt.gz', delete=False
        )

    @unittest.expectedFailure
    def test4(self):
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.txt', f'{currdir}file3.zip', delete=False
        )

    @unittest.expectedFailure
    def test5(self):
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file3.zip', f'{currdir}file1.txt', delete=False
        )

    @unittest.expectedFailure
    def test6(self):
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.zip', f'{currdir}file3.txt', delete=False
        )

    @unittest.expectedFailure
    def test7(self):
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file3.zip', f'{currdir}file3.zip', delete=False
        )

    @unittest.expectedFailure
    def test8(self):
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.zip', f'{currdir}file2.zip', delete=False
        )

    @unittest.expectedFailure
    def test8gz(self):
        self.assertFileEqualsLargeBaseline(
            f'{currdir}file1.txt.gz', f'{currdir}file2.txt.gz', delete=False
        )


if __name__ == "__main__":
    unittest.main()
