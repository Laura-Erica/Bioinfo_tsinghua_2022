#! /bin/bash


input_fa=sequences/five.prime.utrs.spliced.fa
tables=""
while read line
do
	b=${line:0:1}
	if [ "$b" == ">" ]
	then
		name=${line}
#		print "$name"
		flag="1"
#		print "$flag"
	else
		a=$line
#		len=$(echo ${#a})
#		print "$len"
		if [ "${#a}" -ge "10" ] && [ "$flag" == "1" ]
		then
			tables+="\n"
			tables+=${name}
			tables+="\n"
			tables+=${line}
			flag="2"
		else
			flag="2"
			tables+=${line}
		fi
	fi
done <$input_fa
printf "$tables" > five.prime.utrs.spliced.filterd.fa

