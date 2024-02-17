# `c2s2-toolchain`

C2S2's custom toolchain for chip development, built and managed using [EasyBuild](https://easybuild.io/)

## Installation

The only requirement is that EasyBuild is installed. There are a [variety of methods](https://tutorial.easybuild.io/2023-eb-eessi-uk-workshop/easybuild-installation/). On C2S2's server, we built Easybuild as a separate module, noting the additional configurations needed to use `EnvironmentModulesC` as the modules tool:

```bash
# Define installation prefix, and install EasyBuild into it
export EB_TMPDIR=/tmp/$USER/eb_tmp
export EB_DIR=/classes/c2s2/easybuild
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

## Configuring

Configuring your EasyBuild system is also important to tailor it to your system. However, it can be overwhelming; EasyBuild is made to have very little hard-coded, and as such has around 275 configurations.
 
Configuration is most easily done through configuration files. However, EasyBuild only recognizes [specific locations](https://docs.easybuild.io/configuration/#configuration_file); these can be shown with

```bash
eb --show-default-configfiles
```

For C2S2, the system-level location was `/etc/xdg/easybuild.d/*.cfg`. This location was only writeable by `root`, so as to ensure easier customization, we included a symlink here to a configuration file in `/classes/c2s2/easybuild`

To create our configuration file, we started with the output of `eb --confighelp`. From here, we uncommented/included the following sections:

```ini
[config]
# ...
module-syntax=Tcl # Support Tcl modules - not needed if you use Lmod
modules-tool=EnvironmentModulesC # Specify the module tool used on C2S2's server
prefix=/classes/c2s2/easybuild # Have a global path for installations and building
# ...
```

You can verify that these changes took effect by running `eb --show-config` to show all of your current configurations