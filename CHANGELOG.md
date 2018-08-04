# CHANGELOG

This contains changes to the input files with time.

- Starting point: files copied from the SRD calculation input files for simulating LSST SNIa  for 10 year WFD and 10 year DDFs based on minion. The SRD had 1 year simulations which have been ignored. The only change in the first commit is that the specific username `RH_` has been substitued by the generic `USERNAME_` to help not clobber simulations performed by Renee Hlozek. The user is expected to change `USERNAME_` to something more personal and easy to identify. 
- While data files have not been changed, the location has been moved around (and described in the `README.md`). A python package `build_snana_inputs` has been created to facilitate accessing files and having tests.
