#=========================================================================
# shell.nix
#=========================================================================
# C2S2's Nix environment, defined for reproducibility
#
# Author: Aidan McNay
# Date: January 30th, 2024

#-------------------------------------------------------------------------
# Default Packages
#-------------------------------------------------------------------------
# Here, we obtain the up-to-date Nix release (at time of writing) for most
# packages

let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in

#-------------------------------------------------------------------------
# Verilator
#-------------------------------------------------------------------------
# We need to specifically install Verilator 4.036, and therefore need to
# import it specifically
#
# The specific hash for the version was obtained using 
# https://lazamar.co.uk/nix-versions/

let
  verilator_nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/archive/e296e89d75ab8aa1d0eed1c3688883a4f7937515.tar.gz";
  verilator_pkgs = import verilator_nixpkgs { config = {}; overlays = []; };
in

#-------------------------------------------------------------------------
# Other aliases
#-------------------------------------------------------------------------

let sv2v = pkgs.haskellPackages.sv2v; in

#-------------------------------------------------------------------------
# Define our shell
#-------------------------------------------------------------------------

pkgs.mkShell {
  packages = with pkgs; [
               # Version:
    gaw        # 20220315
    git        # 2.42.0
    gperf      # 3.1
    gtkwave    # 3.3.118
    klayout    # 0.28.12
    micro      # 2.0.12
    ngspice    # 41
    magic-vlsi # 8.3.447
    python3    # 3.11.6
    # sv2v       # 0.0.11 - currently marked as broken
    symbiyosys # 2021.11.30
    tmux       # 3.3a
    verilog    # 12.0 (iverilog)
    xclip      # 0.13
    xschem     # 3.4.4
    yosys      # 0.3.5
  ];
}

# #-------------------------------------------------------------------------
# # Python Packages
# #-------------------------------------------------------------------------
# # Here, we customize our Python installation using mach-nix
# #
# # https://github.com/DavHau/mach-nix

# let
#   mach-nix = import (builtins.fetchGit {
#     url = "https://github.com/DavHau/mach-nix";
#     ref = "refs/tags/3.5.0";
#   }) {};
# in
# mach-nix.mkPython {
#   requirements = requirements = builtins.readFile ./requirements.txt;
# };

# #-------------------------------------------------------------------------
# # Other Tools
# #-------------------------------------------------------------------------
# # Here's where we define how to build any other tools that we may need

# environment.systemPackages = [
#     ( pkgs.callPackage ./netgen.nix {} )
# ];