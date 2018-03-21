#!/usr/bin/env python 
import sys
from csv import reader
for line in reader(sys.stdin):
#	line=line.strip()
#	words=line.split(',')
	if line[14]!='T':
		print ('%s, %s\t%s'%(line[14],line[16],1))
