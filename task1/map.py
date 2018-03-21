#!/usr/bin/env python 
import sys
from csv import reader
for line in reader(sys.stdin):
	if len(line) == 18:
               	print('%s\topen'%(line[0]))
	if len(line) == 22:
        	print('%s\t%s, %s, %s, %s'%(line[0],line[14],line[6],line[2],line[1]))
