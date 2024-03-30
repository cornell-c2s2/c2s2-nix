
from easybuild.easyblocks.generic.configuremake import ConfigureMake
from easybuild.framework.easyconfig import CUSTOM
from easybuild.tools.py2vs3 import string_type
from easybuild.tools.run import run_cmd

#=========================================================================
# RISCV GNU Toolchain
#=========================================================================

DEFAULT_BUILD_CMD = 'make'
DEFAULT_BUILD_TARGET = ''

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

        paracmd = ''
        if self.cfg['parallel']:
            paracmd = "-j %s" % self.cfg['parallel']

        targets = self.cfg.get('build_cmd_targets') or DEFAULT_BUILD_TARGET
        # ensure strings are converted to list
        targets = [targets] if isinstance(targets, string_type) else targets
        if self.cfg['with_spike']:
            targets.append( 'build-sim' )

        for target in targets:
            cmd = ' '.join([
                self.cfg['prebuildopts'],
                self.cfg.get('build_cmd') or DEFAULT_BUILD_CMD,
                target,
                paracmd,
                self.cfg['buildopts'],
            ])
            if target == 'build-sim':
                # Make sure to not set flags specific to native GCC
                cmd = "unset CC CXX CFLAGS CXXFLAGS LIBS && " + cmd
                # Make sure pk knows about the RISCV compiler
                cmd = f"export PATH={self.installdir}/bin:$PATH && " + cmd

            self.log.info("Building target '%s'", target)

            (out, _) = run_cmd(cmd, log_all=True, simple=False)

        return out