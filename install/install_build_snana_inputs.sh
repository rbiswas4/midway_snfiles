#!/usr/bin/env bash
gunzip -c build_snana_inputs/data/*.gz #> build_snana_inputs/data/
python setup/generate_requirements.py
python setup.py install --user
