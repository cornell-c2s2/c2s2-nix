
from easybuild.easyblocks.generic.configuremake import ConfigureMake
from easybuild.framework.easyconfig import CUSTOM

#=========================================================================
# RISCV GNU Toolchain
#=========================================================================

class EB_RISCVGNUToolchain(ConfigureMake):
    """
    EasyBlock for building the RISCV GNU Toolchain

    This is just a thin wrapper around ConfigureMake

    We just need to be careful to recognize that the `make` command both
    builds AND installs (similar to what `make install` does), and write
    our EasyBlock such that the install directory isn't wiped early
    """

    def extra_options(extra_vars=None):
        """Extra easyconfig parameters specific to ConfigureMake."""
        extra_vars = ConfigureMake.extra_options(extra_vars=extra_vars)
        extra_vars.update({
            'with_spike': [False, "Whether to include spike when building", CUSTOM],
        })
        return extra_vars

    def build_step(self):
        """We "build" as part of installation - do nothing here"""
        pass

    def install_step(self):
        """Do what `build_step` used to do"""

        if( self.cfg['with_spike'] ):
            self.cfg['build_cmd_targets'] = 'all build-sim'
        return super().build_step( self )