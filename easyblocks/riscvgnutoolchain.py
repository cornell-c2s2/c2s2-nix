
from easybuild.easyblocks.generic.configuremake import ConfigureMake

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

    def build_step(self):
        """We "build" as part of installation - do nothing here"""
        pass

    def install_step(self):
        """Do what `build_step` used to do"""
        return super().build_step( self )