#!/bin/bash

pip3 install termgraph > /dev/null 2> /dev/null
termgraph data.dat --color {green,magenta} --width 90
termgraph data.dat --color {red,cyan}

