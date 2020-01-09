#!/usr/bin/env bash

echo 💣
for i in `seq 5 1`;do
	echo -n -e "このコンピュータはあと${i}秒で爆発します\r"
	sleep 1
done
echo -e "このコンピュータはあと0秒で爆発します\r"
echo 💥
