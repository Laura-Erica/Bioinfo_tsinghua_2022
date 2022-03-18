#!/bin/bash
# retrive all the file names and directory names from a specialized path.

#path input
echo -n 'please input a dictionary;'
read diction

DIC_TO_COUNT=$(ls ./$diction)

for i in $DIC_TO_COUNT
do
#test for successful input
#	echo "$i" 
	if [ -f "./$diction/$i" ]
	then
#test for successful judgement
#		echo "$i is a file"
		echo "$i" >> filename.txt
	elif [ -d "./$diction/$i" ]
	then
#test for successful judgement
#		echo "$i is a dic"
		echo "$i" >> dirname.txt
	fi
done

