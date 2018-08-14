from __future__ import print_function
import numpy as np
import pylab as pl
import sys

''' eg. use as 
python generate_cadences.py YOURPREFIX your/path/to/SIMGEN_MASTER_LSST_XX_Y10_baseline.INPUT ddfcadence.list, depending on if you want DDF or WFD for example. '''
username = sys.argv[1]
cadence_list = sys.argv[3]
input_file = sys.argv[2]

clines = open(cadence_list, 'r').readlines()
ilines = open(input_file, 'r').readlines()
cadences = []

for cl, line in enumerate(clines):
    split = line.split('.')

    cadences.append(split[0]+'.'+split[1])

    output_file = input_file[0:-6] +'_'+ cadences[cl][0:-7]+ '.INPUT'
    print(output_file)
    f = open(output_file, 'w')
    for iline in ilines:
        if 'USERNAME' in iline:
            lline = iline.split('_')
            bline = lline[0].split(':')
            bline[1] = username+'_'+cadences[cl][0:-7]
            cline = ": ".join(bline)
            lline[0]=cline
            iline = "_".join(lline)
#           print(iline)
        
        if 'COADD' in iline:
            lline =  iline.split('.')
            lline[-2] = lline[-2][0:-7]
            lline[-1] = 'cwp/'+cadences[cl]+'.COADD' + '\n'
            iline =  "/".join(lline)
        f.write(iline)

            
