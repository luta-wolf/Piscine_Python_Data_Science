#!/bin/sh

FILE=hh_concatenator.csv

echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > $FILE

for file in 20*.csv
do
tail -n +2 $file >> $FILE
done