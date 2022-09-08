#!/bin/bash
#SBATCH --job-name=a5open
#SBATCH --array=1-1000%100
#SBATCH --output=a5open.txt

module load procheck/3.5.4
#get files on desktop and store into array

CHAINS=("A" "B" "C" "D" "E" "F" "G" "H" "I" "J")

DIRS=(~/pdbs/*)

FILEXT=${DIRS[$SLURM_ARRAY_TASK_ID]}

echo "$FILEXT"

FILE=$(basename ${FILEXT%.*})

mkdir ~/procheck/"$FILE"
cd ~/procheck/"$FILE" || { echo "Directory not found"; exit 1; }
for i in "${CHAINS[@]}"
do
 mkdir ~/procheck/"$FILE"/"$i"
 cd ~/procheck/"$FILE"/"$i" || { echo "Directory not found"; exit 1; }
 procheck $FILEXT "$i" 2.0
done
