#  _________________________________________________________________________
#
#  PyUtilib: A Python utility library.
#  Copyright (c) 2008 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  _________________________________________________________________________
#

import pyutilib.autotest
from pyutilib.component.core import alias
import pyutilib.subprocess


class ExampleTestDriver(pyutilib.autotest.TestDriverBase):
    """
    This test driver executes a unix command and compares its output
    with a baseline value.
    """

    alias('example')

    def run_test(self, testcase, name, options):
        """Execute a single test in the suite"""
        name = f'{options.suite}_{name}'
        cmd = f'{options.solver} '
        if options.cat_options is not None:
            cmd += f'{options.cat_options} '
        cmd += options.file
        print(f"Running test suite '{options.suite}'  test '{name}'  command '{cmd}'")
        pyutilib.subprocess.run(cmd, outfile=f'{options.currdir}test_{name}.out')
        testcase.failUnlessFileEqualsBaseline(
            f'{options.currdir}test_{name}.out',
            f'{options.currdir}test_{name}.txt',
        )
