#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
#USAGE :  python python_mdanalysis_skeleton.py [config file name]                                                                  

#DEPENDCIES : numpy, MDAnalysis, math, sys                                                                                         

#CONFIG FILE FORMAT:                                                                                                               
#   TopFile = [topology file name (prmtop file)]                                                                                   
#   TrajFile = [trajectory file name (mdcrd file)]                                                                                 
#   OutFile = [output data file name]                                                                                              

import numpy as np
import sys
import os
import MDAnalysis
import math
# compute the distance between two points taking into account periodic boundary conditions                                         
def computePbcDist2(r1,r2,box):
        dist2 = 0

        for j in range(0,3):
                temp = r1[j]-r2[j]
                if temp < -box[j]/2.0:
                        temp += box[j]
                elif temp > box[j]/2.0:
                        temp -= box[j]
                dist2 += temp*temp

        return dist2;
# read the configuration file and populate the global variables                                                                    
def ParseConfigFile(cfg_file):
        global top_file, traj_file, out_file
        f = open(cfg_file)
        for line in f:
                # first remove comments                                                                                            
                if '#' in line:
                        line, comment = line.split('#',1)
                if '=' in line:
                        option, value = line.split('=',1)
                        option = option.strip()
                        value = value.strip()
                        print "Option:", option, " Value:", value
                        # check value                                                                                              
                        if option.lower()=='topfile':
                                top_file = value
                        elif option.lower()=='trajfile':
                                traj_file = value
                        elif option.lower()=='outfile':
                                out_file = value
                        else :
                                print "Option:", option, " is not recognized"
        f.close()

# Main Program                                                                                                                     

# read in command line argument                                                                                                    
cfg_file = sys.argv[1]

# read cfg file                                                                                                                    
ParseConfigFile(cfg_file)

print "Topology file:", top_file
print "Trajectory file:", traj_file
print "Output data file:", out_file

# initiate MDAnalysis coordinate universe                                                                                          
coord = MDAnalysis.Universe(top_file, traj_file)
# make an atom selection                                                                                                           
sel_1 = coord.selectAtoms("resid 5")
sel_2 = coord.selectAtoms("resid 14")
print sel_1, sel_1.n_atoms
print sel_2, sel_2.n_atoms

# open output files                                                                                                                
out = open(out_file,'w')

# Loop through trajectory                                                                                                          
for ts in coord.trajectory:
      dist = math.sqrt(computePbcDist2(sel_1.center_of_mass(),sel_2.center_of_mass(),coord.dimensions[:3]))
      
      out.write("%10.5f\n" %(dist))

# close output file                                                                                                                
out.close
