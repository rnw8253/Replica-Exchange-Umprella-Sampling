# Replica-Exchange-Umprella-Sampling


vmd.namdcoorsave and NAMD.write.coor.tcl are used to convert AMBER restart files to NAMD binary positions file

com_EAAAG.conf 	  - length of trajectories, # of runs and collective variable
colvars.conf   	  - defines the collective variables  
EAAAG_base.namd   - simulation parameters in NAMD
job0.conf 	  - first run of REUS from equilibrated windows with restraint
job1.conf   	  - used to continue runs
replica.namd.tcl  - needed to run REUS

sort_replicas.sh is used to sort each trajectory so that it only contains one harmonic constraint

All COM_distance files are used to extract COM_distance between a given atom selection in a trajectory