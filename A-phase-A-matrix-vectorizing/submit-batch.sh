#!/bin/bash -l
#SBATCH --job-name=btest   # Job name
#SBATCH --output=btest.o%j # Name of stdout output file
#SBATCH --error=btest.e%j  # Name of stderr error file
#SBATCH --partition=small    # partition name
#SBATCH --nodes=1               # Total number of nodes
#SBATCH --ntasks=1            # Total number of mpi tasks
#SBATCH --mem=64G                 # Allocate all the memory on each node
#SBATCH --time=0-10:00:00       # Run time (d-hh:mm:ss)
#SBATCH --account=project_462000960  # Project for billing

# All commands must follow the #SBATCH directives

# Launch MPI code 
srun pvbatch dyGiLa-phase-cluster-distribution-counting.py # Use srun instead of mpirun or mpiexec
