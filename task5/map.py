#!/usr/bin/env python 
import sys
for line in sys.stdin:
	line=line.strip()
	words=line.split(',')
	print  ('%s, %s\t%s'%(words[14],words[16],1))
