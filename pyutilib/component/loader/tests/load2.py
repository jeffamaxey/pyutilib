import pyutilib.misc
import pyutilib.component.core
import os
import sys

currdir = sys.argv[-2] + os.sep

pyutilib.component.core.PluginGlobals.get_env().load_services(
    path=[f"{currdir}plugins1", f"{currdir}plugins2"]
)
pyutilib.misc.setup_redirect(f"{currdir}load2.out")
if sys.argv[-1] == "json":
    pyutilib.component.core.PluginGlobals.pprint(json=True)
else:
    pyutilib.component.core.PluginGlobals.pprint()
pyutilib.misc.reset_redirect()
