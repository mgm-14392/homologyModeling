#!/bin/bash
#SBATCH --job-name=a5closed
#SBATCH --array=1-1000%100
#SBATCH --output=a5closed.txt

module load Python/3.6.8
module load modeller/9.23-python3.3-8

rootdir=`pwd`

echo "My SLURM_ARRAY_TASK_ID: $SLURM_ARRAY_TASK_ID"

#echo "$baseFilename"

mkdir -p $rootdir/Model_closed${SLURM_ARRAY_TASK_ID} && cp ali_t3-6.pir "$_"

cd $rootdir/Model_closed${SLURM_ARRAY_TASK_ID} || { echo "Directory not found"; exit 1; }

python3 $rootdir/modelMGM.py ali_t3-6.pir > closed.txt

cd $rootdir || { echo "Directory not found"; exit 1; }