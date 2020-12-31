#! /bin/bash

echo "File name: "
read filename

if [[ -f $filename ]]
then
	awk '/Linux/ {print dsad}' $filename
else
	echo "$filename doesn't exist"
fi
