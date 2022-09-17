#!/bin/sh

(cat $1 | head -n 1; cat $1 | tail -n +2 | sort -t "," -k2 -k1) > hh_sorted.csv