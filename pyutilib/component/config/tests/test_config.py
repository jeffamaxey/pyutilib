#
# Unit Tests for pyutilib.options.configuration
#
#

import os
import sys
from os.path import abspath, dirname
currdir = dirname(abspath(__file__)) + os.sep

from nose.tools import nottest
from pyutilib.component.core import ExtensionPoint, Plugin, PluginGlobals
from pyutilib.component.config.options import FileOption, declare_option
from pyutilib.component.config import Configuration, ConfigurationError
import pyutilib.th as unittest
import pyutilib.misc


def filter(line):
    return line.startswith(
        ";   section='") or 'memmon' in line or 'valgrind' in line or '[executables]' in line or 'null' in line


class Test(unittest.TestCase):

    class TMP(Plugin):

        def __init__(self):
            declare_option("a")
            declare_option("b", local_name="bb")
            declare_option("b")
            declare_option("c")
            declare_option("zz", section='a.b')
            declare_option("yy", default="foo")

    def setUp(self):
        PluginGlobals.add_env("testing.config")
        pyutilib.component.config.plugin_ConfigParser.Configuration_ConfigParser(
            name="Configuration_ConfigParser")
        self.tmp = Test.TMP()

    def tearDown(self):
        del self.tmp
        PluginGlobals.remove_env(
            "testing.config", cleanup=True, singleton=False)

    def test_init(self):
        """Test Configuration construction"""
        config = Configuration()

    def test_contains(self):
        """Test contains method"""
        config = Configuration()
        self.assertFalse("globals" in config)
        config.load(f"{currdir}config1.ini")
        self.assertTrue("globals" in config)

    def test_getitem(self):
        """Test getitem method"""
        config = Configuration()
        try:
            config["globals"]
            self.fail("expected error")
        except ConfigurationError:
            pass
        config.load(f"{currdir}config1.ini")
        keys = sorted(config["globals"].keys())
        self.assertTrue(keys == ["a", "b", "c"])

    def test_sections(self):
        """Test getitem method"""
        config = Configuration()
        config.load(f"{currdir}config1.ini")
        keys = sorted(config.sections())

    def test_load1(self):
        """Test load method"""
        config = Configuration()
        try:
            config.load(None)
            self.fail("expected error")
        except ConfigurationError:
            pass

    def test_load2(self):
        """Test load method"""
        config = Configuration()
        try:
            config.load("__missing__")
            self.fail("expected error")
        except ConfigurationError:
            pass

    def test_load3(self):
        """Test load method"""
        config = Configuration()
        try:
            config.load(f"{currdir}config2.ini")
            config.pprint()
            self.fail("expected error")
        except ConfigurationError:
            pass

    def test_load4(self):
        """Test load method"""
        config = Configuration()
        try:
            config.load(f"{currdir}config3.ini")
            self.fail("expected error")
        except ConfigurationError:
            pass

    def test_load5(self):
        """Test load method"""
        PluginGlobals.add_env("testing.config_loading")

        class TMP2(Plugin):

            def __init__(self):
                declare_option("a")
                declare_option("b", cls=FileOption)
                declare_option("c")
                declare_option("xx", section_re='globals.*')

        config = Configuration()
        tmp2 = TMP2()
        config.load(f"{currdir}config4.ini")
        #PluginGlobals.pprint()
        config.save(f"{currdir}config4.out")
        #print config
        self.assertFileEqualsBaseline(
            f"{currdir}config4.out", f"{currdir}config4.txt", filter=filter
        )
        pyutilib.misc.setup_redirect(f"{currdir}log2.out")
        config.pprint()
        pyutilib.misc.reset_redirect()
        self.assertFileEqualsBaseline(
            f"{currdir}log2.out", f"{currdir}log2.txt", filter=filter
        )
        PluginGlobals.remove_env(
            "testing.config_loading", cleanup=True, singleton=False)

    def test_save1(self):
        """Test save method"""
        config = Configuration()
        config.load(f"{currdir}config1.ini")
        config.save(f"{currdir}config1.out")
        #PluginGlobals.pprint()
        self.assertFileEqualsBaseline(
            f"{currdir}config1.out", f"{currdir}config1.txt", filter=filter
        )

    def test_save2(self):
        """Test save method"""
        config = Configuration()
        try:
            config.save(None)
            self.fail("expected error")
        except ConfigurationError:
            pass


if __name__ == "__main__":
    unittest.main()
