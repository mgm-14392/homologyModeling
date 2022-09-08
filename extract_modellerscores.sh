#!/bin/bash

DIR=`pwd`

# extract results form .txt files generated while running modeller
for file in $DIR/*.txt;
do
 NAME=`basename $file .txt`
 # the scores are in the last 5 rows
 line=$(sed -n -e '/^closed.B99990001.pdb/p' $file)
 echo "$NAME ""$line" >> modeller_scores.out
done

# remove second column
awk '{print $1" "$3" "$4" "$5" "$6}' modeller_scores.out > temp.out && mv temp.out modeller_scores.out
# sort by zDOPE score
sort -k5 -n modeller_scores.out > temp.out && mv temp.out modeller_scores.out
# add header with scores names
sed  -i '1i FILE MOLPDF DOPE GA341 zDOPE' modeller_scores.out