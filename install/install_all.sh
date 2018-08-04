#!/usr/bin/env bash
echo "installing dependencies from pip"
./install/install_pip_requirements.sh
echo "installing dependencies from conda"
./install/install_conda_requirements.sh
echo "Done installing repositories"
echo "Install build_snana_inputs"
./install/install_build_snana_inputs.sh


