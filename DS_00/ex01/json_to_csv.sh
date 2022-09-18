#!/bin/sh

# cat $1 | jq -rf filter.jq > hh.csv

jq '.items' ../ex00/hh.json | jq -r -f filter.jq > hh.csv
