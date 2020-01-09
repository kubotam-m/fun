#! /usr/bin/env bash
datafile=test_dict.txt
n=`cut -f1 $datafile | grep -n ${@} |cut -f 1 -d ":"`
if [ "${n}" = "" ] ; then
	echo "not found"
else
	echo $n|xargs -n 1 -I num sed -n nump $datafile|grep --color=auto $@
	#echo $n|xargs -n 1 -I num sed -n nump $datafile|cut -f 2-
	#sed -n ${n}p $datafile|cut -f 2-
fi

