#
# Unit Tests for pyutilib.options.configuration
#
#

import glob
import sys
import shutil
import os
from os.path import abspath, dirname
currdir = dirname(abspath(__file__)) + os.sep
tempdir = dirname(abspath(__file__)) + os.sep + 'tempdir' + os.sep

from pyutilib.component.config import *
import pyutilib.th as unittest

old_tempdir = TempfileManager.tempdir


class Test(unittest.TestCase):

    def setUp(self):
        PluginGlobals.add_env("testing.options")
        TempfileManager.tempdir = tempdir
        TempfileManager.push()
        if os.path.exists(tempdir):
            shutil.rmtree(tempdir)
        os.mkdir(tempdir)

    def tearDown(self):
        TempfileManager.pop()
        TempfileManager.tempdir = old_tempdir
        PluginGlobals.remove_env("testing.options")
        if os.path.exists(tempdir):
            shutil.rmtree(tempdir)

    def test_add1(self):
        """Test explicit adding of a file that is missing"""
        try:
            TempfileManager.add_tempfile(f'{tempdir}add1')
            self.fail("Expected IOError because file 'add1' does not exist")
        except IOError:
            pass

    def test_add1_dir(self):
        """Test explicit adding of a directory that is missing"""
        try:
            TempfileManager.add_tempfile(f'{tempdir}add1')
            self.fail(
                "Expected IOError because directory 'add1' does not exist")
        except IOError:
            pass

    def test_add2(self):
        """Test explicit adding of a file that is missing"""
        TempfileManager.add_tempfile(f'{tempdir}add2', False)

    def test_add2_dir(self):
        """Test explicit adding of a directory that is missing"""
        TempfileManager.add_tempfile(f'{tempdir}add2', False)

    def test_add3(self):
        """Test explicit adding of a file that already exists"""
        with open(f'{tempdir}add3', 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        TempfileManager.add_tempfile(f'{tempdir}add3')

    def test_add3_dir(self):
        """Test explicit adding of a directory that already exists"""
        os.mkdir(f'{tempdir}add3')
        TempfileManager.add_tempfile(f'{tempdir}add3')

    def test_pushpop1(self):
        """Test pushpop logic"""
        TempfileManager.push()
        with open(f'{tempdir}pushpop1', 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        TempfileManager.add_tempfile(f'{tempdir}pushpop1')
        TempfileManager.pop()
        if os.path.exists(f'{tempdir}pushpop1'):
            self.fail("pop() failed to clean out files")

    def test_pushpop1_dir(self):
        """Test pushpop logic with directories"""
        TempfileManager.push()
        os.mkdir(f'{tempdir}pushpop1')
        TempfileManager.add_tempfile(f'{tempdir}pushpop1')
        TempfileManager.pop()
        if os.path.exists(f'{tempdir}pushpop1'):
            self.fail("pop() failed to clean out directories")

    def test_pushpop2(self):
        """Test pushpop logic"""
        TempfileManager.push()
        with open(f'{tempdir}pushpop2', 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        TempfileManager.add_tempfile(f'{tempdir}pushpop2')

        TempfileManager.push()
        with open(f'{tempdir}pushpop2a', 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        TempfileManager.add_tempfile(f'{tempdir}pushpop2a')
        TempfileManager.pop()
        if not os.path.exists(f'{tempdir}pushpop2'):
            self.fail("pop() clean out all files")
        if os.path.exists(f'{tempdir}pushpop2a'):
            self.fail("pop() failed to clean out files")

        TempfileManager.pop()
        if os.path.exists(f'{tempdir}pushpop2'):
            self.fail("pop() failed to clean out files")

    def test_pushpop2_dir(self):
        """Test pushpop logic with directories"""
        TempfileManager.push()
        os.mkdir(f'{tempdir}pushpop2')
        TempfileManager.add_tempfile(f'{tempdir}pushpop2')

        TempfileManager.push()
        os.mkdir(f'{tempdir}pushpop2a')
        TempfileManager.add_tempfile(f'{tempdir}pushpop2a')
        TempfileManager.pop()
        if not os.path.exists(f'{tempdir}pushpop2'):
            self.fail("pop() clean out all files")
        if os.path.exists(f'{tempdir}pushpop2a'):
            self.fail("pop() failed to clean out files")

        TempfileManager.pop()
        if os.path.exists(f'{tempdir}pushpop2'):
            self.fail("pop() failed to clean out files")

    def test_clear(self):
        """Test clear logic"""
        TempfileManager.push()
        with open(f'{tempdir}pushpop2', 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        os.mkdir(f'{tempdir}pushpopdir2')
        TempfileManager.add_tempfile(f'{tempdir}pushpop2')
        TempfileManager.add_tempfile(f'{tempdir}pushpopdir2')

        TempfileManager.push()
        with open(f'{tempdir}pushpop2a', 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        os.mkdir(f'{tempdir}pushpopdir2a')
        TempfileManager.add_tempfile(f'{tempdir}pushpop2a')
        TempfileManager.add_tempfile(f'{tempdir}pushpopdir2a')

        TempfileManager.clear_tempfiles()

        if os.path.exists(f'{tempdir}pushpop2a'):
            self.fail("clear_tempfiles() failed to clean out files")
        if os.path.exists(f'{tempdir}pushpopdir2a'):
            self.fail("clear_tempfiles() failed to clean out directories")
        if os.path.exists(f'{tempdir}pushpop2'):
            self.fail("clear_tempfiles() failed to clean out files")
        if os.path.exists(f'{tempdir}pushpopdir2'):
            self.fail("clear_tempfiles() failed to clean out directories")

    def test_create1(self):
        """Test create logic - no options"""
        fname = TempfileManager.create_tempfile()
        with open(fname, 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 1)
        fname = os.path.basename(fname)
        self.assertTrue(fname.startswith('tmp'))

    def test_create1_dir(self):
        """Test create logic - no options"""
        fname = TempfileManager.create_tempdir()
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 1)
        fname = os.path.basename(fname)
        self.assertTrue(fname.startswith('tmp'))

    def test_create1a(self):
        """Test create logic - no options"""
        fname = TempfileManager.create_tempfile(dir=tempdir)
        with open(fname, 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 1)
        fname = os.path.basename(fname)
        self.assertTrue(fname.startswith('tmp'))

    def test_create1a_dir(self):
        """Test create logic - no options"""
        fname = TempfileManager.create_tempdir(dir=tempdir)
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 1)
        fname = os.path.basename(fname)
        self.assertTrue(fname.startswith('tmp'))

    def test_create2(self):
        """Test create logic - no options"""
        fname = TempfileManager.create_tempfile(prefix='foo')
        with open(fname, 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 1)
        fname = os.path.basename(fname)
        self.assertTrue(fname.startswith('foo'))

    def test_create2_dir(self):
        """Test create logic - no options"""
        fname = TempfileManager.create_tempdir(prefix='foo')
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 1)
        fname = os.path.basename(fname)
        self.assertTrue(fname.startswith('foo'))

    def test_create3(self):
        """Test create logic - no options"""
        fname = TempfileManager.create_tempfile(suffix='bar')
        with open(fname, 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 1)
        fname = os.path.basename(fname)
        self.assertTrue(fname.endswith('bar'))

    def test_create3_dir(self):
        """Test create logic - no options"""
        fname = TempfileManager.create_tempdir(suffix='bar')
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 1)
        fname = os.path.basename(fname)
        self.assertTrue(fname.endswith('bar'))

    def test_create4(self):
        """Test create logic - no options"""
        TempfileManager.sequential_files(2)
        fname = TempfileManager.create_tempfile()
        with open(fname, 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 1)
        fname = os.path.basename(fname)
        self.assertEqual(fname, 'tmp2')
        #
        TempfileManager.unique_files()
        fname = TempfileManager.create_tempfile()
        with open(fname, 'w') as OUTPUT:
            OUTPUT.write('tempfile\n')
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 2)
        fname = os.path.basename(fname)
        self.assertNotEqual(fname, 'tmp3')
        self.assertTrue(fname.startswith('tmp'))

    def test_create4_dir(self):
        """Test create logic - no options"""
        TempfileManager.sequential_files(2)
        fname = TempfileManager.create_tempdir()
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 1)
        fname = os.path.basename(fname)
        self.assertEqual(fname, 'tmp2')
        #
        TempfileManager.unique_files()
        fname = TempfileManager.create_tempdir()
        self.assertEqual(len(list(glob.glob(f'{tempdir}*'))), 2)
        fname = os.path.basename(fname)
        self.assertNotEqual(fname, 'tmp3')
        self.assertTrue(fname.startswith('tmp'))


if __name__ == "__main__":
    unittest.main()
