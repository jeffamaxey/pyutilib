import pyutilib.component.app
import os
import sys

currdir = sys.argv[-1] + os.sep

app = pyutilib.component.app.SimpleApplication("foo")
app.config.load(f"{currdir}config1.txt")
app.config.save(f"{currdir}config1.out")
