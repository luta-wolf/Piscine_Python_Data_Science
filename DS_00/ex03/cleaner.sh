#!/bin/sh

INPUT_FILE="../ex02/hh_sorted.csv"
OUTPUT_FILE="hh_positions.csv"

# pass headers
cat $INPUT_FILE \
  | head -n 1 \
  > $OUTPUT_FILE

tail -n +2 $INPUT_FILE | \
awk 'BEGIN { FS = OFS = "," }
    {
        STR = ""
        if (index(tolower($3), "junior"))
            STR = STR"Junior/"
        if (index(tolower($3), "middle"))
            STR = STR"Middle/"
        if (index(tolower($3), "senior"))
            STR = STR"Senior"
        if (STR == "")
            STR = "-"
        gsub(/[\/ ]*$/, "", STR)

        $3 = "\""STR"\""
        print
    }' \
    >> $OUTPUT_FILE
