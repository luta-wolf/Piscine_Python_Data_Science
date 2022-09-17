#!/bin/sh

FILE=../ex03/hh_positions.csv

echo '"name","count"' > hh_uniq_positions.csv
tail -n +2 $FILE | cut -f 3 -d ',' | sort | uniq -ci | sort -nr | awk -F ' \"' '{print "\""$2","$1}' | sed -E 's/, +/,/g' >> hh_uniq_positions.csv

sed -i '' '/-/d' hh_uniq_positions.csv