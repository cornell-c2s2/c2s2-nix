
import os
import shutil
import stat

from easybuild.easyblocks.generic.tarball import Tarball
from easybuild.tools.run import run_cmd
from easybuild.framework.easyconfig import CUSTOM

#=========================================================================
# Klayout
#=========================================================================

class EB_Klayout(Tarball):
    """
    EasyBlock for building KLayout binaries to the installation directory
    """

    # Default to building without Python or Ruby - might want to change in future
    # (not very customizable in general, but works for now)

    @staticmethod
    def extra_options():
        extra_vars = {
            'qmake_path': ["$EBROOTQT6/bin/qmake", "Path to the QMake binary", CUSTOM],
            'use_ccache': [True, "Whether to use ccache to optimize compile time", CUSTOM],
        }
        extra_vars = Tarball.extra_options(extra_vars)
        return extra_vars

    def install_step(self):

        # Use ccache if necessary
        if self.cfg['qmake_path']:
            install_cmd = "export QMAKE_CCACHE=1 && "
        else:
            install_cmd = ""

        install_cmd += f"./build.sh -noruby -nopython"
        install_cmd += f" -option -j{self.cfg['parallel']}"
        install_cmd += f" -qmake {self.cfg['qmake_path']}"

        bindir = os.path.join(self.installdir, 'bin')
        install_cmd += f" -prefix {bindir}"
        try:
            os.makedirs(bindir)
            (out, _) = run_cmd(install_cmd, log_all=True, simple=False)
        except OSError as err:
            raise EasyBuildError("Installing KLayout binaries in %s failed: %s", bindir, err)

        return out