#!/bin/bash

echo Swap!
for i in {10..1}; do
	echo $i
	sleep 1
done
echo 
python queuetemp.py

