#!/usr/bin/env python 
import sys
from csv import reader
for line in reader(sys.stdin):
#	line=line.strip()
#	words=line.split(',')
	if len(line)==22:
		state=line[16]		
		if state!='NY':
			state='Other'
		print ("%s"%(state))

