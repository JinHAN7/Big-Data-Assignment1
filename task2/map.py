#!/usr/bin/env python
import sys
#import numpy as np 
#import pandas as pd 
#import string
for line in sys.stdin:
	line=line.strip()
	words=line.split(',')
	print ("%s\t%s"%(words[2],1))

