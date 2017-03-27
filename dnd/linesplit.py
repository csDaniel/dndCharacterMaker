#!/usr/bin/python

import os

def splitline():
	with open('races') as fd:
		content = fd.read().split(', ')
	fd.close()

	fd = open('char stats', 'w')
	for c in content:
		fd.write(c)
		fd.write(',\n')

	fd.close()
splitline()