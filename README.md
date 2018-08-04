# INPUT FILES FOR SNANA simulations of LSST on MIDWAY

These are input files used on midway to produce LSST simulations for the WFD and DDF fields for 10 years on midway. The contents, usage and evolution of these files is explained below.

## CONTENTS
1. SIMGEN_MASTER_LSST_DDF_Y10.INPUT : Master input file for `LSST_DDF`
2. SIMGEN_MASTER_LSST_WFD_Y10.INPUT : Master input file for `LSST_WFD` 
3. SIMGEN_SALT2_POPCHAR.INPUT : Input file describing Ia (SALT Model) population

## Usage  
To use these files, a user should change the GENVERSION on the `SIMGEN_MASTER_LSST_DDF_Y10.INPUT` and `SIMGEN_MASTER_LSST_WFD_Y10.INPUT`. The minimal change required is to change `USERNAME_` to a name that identifies a user.  

To run the simulations on midway : run 
```
nohup sim_SNmix.pl SIMGEN_MASTER_LSST_WFD_Y10.INPUT > ${USER}_WFD.log 2>&1 & 
nohup sim_SNmix.pl SIMGEN_MASTER_LSST_DDF_Y10.INPUT > ${USER}_WFD.log 2>&1 & 
```

## PROVENANCE
These files are being maintained from the SRD simulations by Renee Hlozek and Dan Scolnic, and the explanations collected in their document `README_BaselineSimulation`. For evolution of these files, please see [CHANGELOG.md](./CHANGELOG.md)
