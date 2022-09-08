#!/bin/bash

module load Python/3.6.8
module load modeller/9.23-python3.3-8

for i in {1..100}
do
 python3 modelMGM.py des_a7.pir > des_"$i".txt
 mv des.B99990001.pdb des_"$i".pdb
 echo "des_$i.pdb"
done
