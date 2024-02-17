# `c2s2-toolchain`

C2S2's custom toolchain for chip development, built and managed using [EasyBuild](https://easybuild.io/)

## Installation

The only requirement is that EasyBuild is installed. There are a [variety of methods](https://tutorial.easybuild.io/2023-eb-eessi-uk-workshop/easybuild-installation/). On C2S2's server, we built Easybuild as a separate module, noting the additional configurations needed to use `EnvironmentModulesC` as the modules tool:

```bash
# Define installation prefix, and install EasyBuild into it
export EB_TMPDIR=/tmp/$USER/eb_tmp
export EB_DIR=/classes/c2s2/easybuild_modules
python3.6 -m pip install --ignore-installed --prefix $EB_TMPDIR easybuild

# Update environment to use this temporary EasyBuild installation
export PATH=$EB_TMPDIR/bin:$PATH
export PYTHONPATH=$EB_TMPDIR/lib/python3.8/site-packages/:$PYTHONPATH
export EB_PYTHON=python3.8

# Install EasyBuild module in C2S2's directory
eb --install-latest-eb-release --prefix $EB_DIR --modules-tool=EnvironmentModulesC --module-syntax=Tcl
```

Once EasyBuild is built as a module, we can inform the module tool of its location, then source the module

```bash
module use $EB_DIR/modules/all
module load EasyBuild
```