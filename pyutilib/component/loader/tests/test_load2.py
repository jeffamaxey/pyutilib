#
# Plugin load tests, with the sys.path loader disabled.
#

import os
import sys
from os.path import abspath, dirname
currdir = dirname(abspath(__file__)) + os.sep

import pyutilib.th as unittest
import pyutilib.subprocess

try:
    import yaml
    yaml_available = True
except ImportError:
    yaml_available = False


class Test(unittest.TestCase):

    def test_load1(self):
        pyutilib.subprocess.run(
            [sys.executable, currdir + os.sep + "load1.py", currdir, "json"])
        self.assertMatchesJsonBaseline(f"{currdir}load1.out", f"{currdir}load1.jsn")
        if yaml_available:
            pyutilib.subprocess.run([sys.executable, currdir + os.sep +
                                     "load1.py", currdir, "yaml"])
            self.assertMatchesYamlBaseline(f"{currdir}load1.out", f"{currdir}load1.yml")

    def test_load1a(self):
        pyutilib.subprocess.run(
            [sys.executable, currdir + os.sep + "load1a.py", currdir, "json"])
        self.assertMatchesJsonBaseline(f"{currdir}load1a.out", f"{currdir}load1a.jsn")
        if yaml_available:
            pyutilib.subprocess.run([sys.executable, currdir + os.sep +
                                     "load1a.py", currdir, "yaml"])
            self.assertMatchesYamlBaseline(f"{currdir}load1a.out", f"{currdir}load1a.yml")

    def test_load2(self):
        pyutilib.subprocess.run(
            [sys.executable, currdir + os.sep + "load2.py", currdir, "json"])
        self.assertMatchesJsonBaseline(f"{currdir}load2.out", f"{currdir}load2.jsn")
        if yaml_available:
            pyutilib.subprocess.run([sys.executable, currdir + os.sep +
                                     "load2.py", currdir, "yaml"])
            self.assertMatchesYamlBaseline(f"{currdir}load2.out", f"{currdir}load2.yml")

    def test_load2a(self):
        pyutilib.subprocess.run(
            [sys.executable, currdir + os.sep + "load2a.py", currdir, "json"])
        self.assertMatchesJsonBaseline(f"{currdir}load2a.out", f"{currdir}load2a.jsn")
        if yaml_available:
            pyutilib.subprocess.run([sys.executable, currdir + os.sep +
                                     "load2a.py", currdir, "yaml"])
            self.assertMatchesYamlBaseline(f"{currdir}load2a.out", f"{currdir}load2a.yml")


if __name__ == "__main__":
    unittest.main()
