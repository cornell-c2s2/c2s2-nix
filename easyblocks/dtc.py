
from easybuild.framework.easyblock import EasyBlock
from easybuild.tools.run import run_cmd

#=========================================================================
# Device Tree Compiler
#=========================================================================

class EB_Dtc(EasyBlock):
    """
    EasyBlock for building the Device Tree Compiler

    We just need to be careful to recognize that the `make install` command
    both builds AND installs, and write our EasyBlock such that the install 
    directory isn't wiped early
    """

    def configure_step(self):
        """We don't need to configure - do nothing here"""
        pass
    
    def build_step(self):
        """We "build" as part of installation - do nothing here"""
        pass

    def install_step(self):
        """Both build and install"""

        install_cmd = f"make install PREFIX={self.installdir}"

        cmd = ' '.join([
            self.cfg['preinstallopts'],
            install_cmd,
            self.cfg['installopts'],
        ])

        (out, _) = run_cmd(cmd, log_all=True, simple=False)

        return out