#!/bin/sh

INPUT_FILE="../ex03/hh_positions.csv"
OUTPUT_FILE="hh_uniq_positions.csv"

echo "\"name\"","\"count\"" > $OUTPUT_FILE
(tail -n +2 $INPUT_FILE | \
awk 'BEGIN { FS = OFS = "," }
    {
        if (index($3, "Junior"))
            JUN++
        if (index($3, "Middle"))
            MID++
        if (index($3, "Senior"))
            SEN++
    }
    END { print "\"Junior\"",
                JUN "\n\"Middle\"",
                MID "\n\"Senior\"", SEN }
    ') | \
    sort -t',' -nk1\
    >>  $OUTPUT_FILE
