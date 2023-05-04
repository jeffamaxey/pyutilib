__all__ = ['ExecutableResource']

import os.path
from pyutilib.workflow import resource
import pyutilib.services
import pyutilib.subprocess

# TODO: add support for logging


class ExecutableResource(resource.Resource):

    def __init__(self, name=None, executable=None):
        resource.Resource.__init__(self)
        if name is None and executable is not None:
            name = os.path.basename(executable)
        if executable is None:
            executable = name
        self.register(name, executable)

    def register(self, name, executable):
        self.filename = executable
        if name is None:
            # TBD: when is this branch executed?
            self.description = f"Executable{self.id}"
            self.name = self.description
        else:
            self.description = f"Executable_{name}"
            self.name = name
        pyutilib.services.register_executable(executable)

    def run(self, args, logfile=None, debug=False):
        executable = pyutilib.services.registered_executable(self.filename)
        if executable is None:
            # TBD: tests generating this error do not cause global exceptions in a workflow ...
            raise IOError(f"Cannot find executable '{self.filename}'")
        cmd = f"{executable.get_path()} {args}"
        if debug:
            print(f"Running... {cmd}")
        pyutilib.subprocess.run(cmd, outfile=logfile)

    def available(self):
        return pyutilib.services.registered_executable(     self.filename) is not None
