#!/bin/bash

for file in *.png;
do
    echo $file
    convert -quality 100 $file eps2:`echo $file | sed -e 's/\.png/\.eps/g'`
done
