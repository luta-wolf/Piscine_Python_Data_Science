#!/bin/sh

cat $1 | jq -rf filter.jq > hh.csv