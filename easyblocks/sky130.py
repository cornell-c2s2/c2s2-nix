
import os
import shutil
import stat

from easybuild.framework.easyblock import EasyBlock
from easybuild.tools.run import run_cmd
from easybuild.framework.easyconfig import CUSTOM

#=========================================================================
# Skywater 130
#=========================================================================

class EB_Sky130(EasyBlock):
    """
    Run the Volare command to build in the install directory
    """

    # Default to building without Python or Ruby - might want to change in future
    # (not very customizable in general, but works for now)

    @staticmethod
    def extra_options():
        extra_vars = {
            'pdk': ["sky130", "PDK to install", CUSTOM],
            'commit': ["78b7bc32ddb4b6f14f76883c2e2dc5b5de9d1cbc", 
                       "Open PDKs commit to use", CUSTOM],
        }
        extra_vars = EasyBlock.extra_options(extra_vars)
        return extra_vars

    def configure_step():
        "Nothing to do"
        pass

    def build_step():
        "Nothing to do"
        pass

    def install_step(self):

        # Use ccache if necessary
        pdk = self.cfg['pdk']
        commit = self.cfg['commit']

        bindir = os.path.join(self.installdir, 'bin')
        install_cmd = f"export PDK_ROOT={bindir} && "

        install_cmd += f"volare enable --pdk {pdk} {commit}"
        try:
            os.makedirs(bindir)
            (out, _) = run_cmd(install_cmd, log_all=True, simple=False)
        except OSError as err:
            raise EasyBuildError("Installing Skywater130 in %s failed: %s", bindir, err)

        return out