import numpy as np
import pylab as pl
import sys

''' eg. use as python generate_cadences.py  data/simInput/SIMGEN_MASTER_LSST_DDF_Y10_baseline.INPUT wfdcadence.list '''

cadence_list = sys.argv[2]
input_file = sys.argv[1]


clines = open(cadence_list, 'r').readlines()
ilines = open(input_file, 'r').readlines()
cadences = []

for cl, line in enumerate(clines):
    split = line.split('.')
    cadences.append(split[0]+'.'+split[1])

#    output_file = input_file
    for iline in ilines:
        if 'COADD' in iline:
            lline =  iline.split('.')
            lline[-2] = lline[-2][0:-7]
            lline[-1] = 'cwp/'+cadences[cl]+'.COADD'
            print "/".join(lline)
    
