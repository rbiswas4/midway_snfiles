conda install --no-update-dependencies -c anaconda -v --yes --file ./install/conda_requirements_anaconda.txt
conda install --no-update-dependencies -c conda-forge -v --yes --file ./install/conda_requirements_conda_forge.txt
conda list --explicit > ./install/spec-file.txt;
