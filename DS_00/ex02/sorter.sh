#!/bin/sh

INPUT_FILE="../ex01/hh.csv"
OUTPUT_FILE="hh_sorted.csv"

# pass headers
cat $INPUT_FILE \
  | head -n 1 \
  > $OUTPUT_FILE

# sort
cat $INPUT_FILE \
  | tail -n +2 \
  | sort -t ',' -k2,2 -k1,1 \
  >> $OUTPUT_FILE

# (head -n 1 $INPUT_FILE; \
#  tail -n +2 $INPUT_FILE \
#  | sort -t ',' -k2,2 -k1,1) \
#  > $OUTPUT_FILE
