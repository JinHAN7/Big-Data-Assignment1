#!/usr/bin/env python 
import sys
from csv import reader
for line in reader(sys.stdin):
#	line=line.strip()
#	words=line.split(',')
	color=line[19]
	make=line[20]	
	make='NONE' if make==''else make
	color='NONE' if color==''else color
	print ('%s,%s'%('vehicle_color',color))
	print ('%s,%s'%('vehicle_make',make))
