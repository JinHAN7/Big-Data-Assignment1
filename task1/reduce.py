#!/usr/bin/env python 
#from operator import itemgetter
import sys

currentkey=None
for line in sys.stdin:
	line=line.strip()
	key,value=line.split('\t')
	if key ==currentkey:
		currentvalue+=value
	else:
		if currentkey:
			if 'open' not in currentvalue:
				 print('%s\t%s'%(currentkey,currentvalue))	
		currentkey=key
		currentvalue=value
if key==currentkey:
	if 'open' not in currentvalue:
		print('%s\t%s'%(currentkey,currentvalue))
		
