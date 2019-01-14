#!/bin/bash
#SBATCH
#SBATCH --array=1-1
#SBATCH --mem=50000
#SBATCH -t 6:00:00

chmod +x job_files/job_${SLURM_ARRAY_TASK_ID}.txt
job_files/job_${SLURM_ARRAY_TASK_ID}.txt
