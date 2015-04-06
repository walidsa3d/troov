#!/usr/bin/env python
#walid.saad

import argparse
import re
import os

db_path='/home/walid/Desktop/files.db'
rootdir='/home/walid/Desktop/'

def update_db():
	files=[]
	for dirName, subdirList, fileList in os.walk(rootdir):
		for fname in fileList:
			filepath=os.path.abspath(os.path.join(dirName, fname))
			files.append(filepath)
	with open(db_path,'w') as f:
		for filepath in files:
			f.write(filepath+'\n')

def find(query):
	occurrences=[]
	with open(db_path) as f:
		for line in f.readlines():
			match = re.search(query, line)
			if match:
				occurrences.append(line)
	return occurrences
def count(query):
	c=0
	with open(db_path) as f:
		for line in f.readlines():
			match = re.search(query, line)
			if match: c=c+1
	return c
def unfind(query):
	occurrences=[]
	with open(db_path) as f:
		for line in f.readlines():
			match = re.search(query, line)
			if not match:
				occurrences.append(line)
	return occurrences

def fprint(lines):
	for line in lines:
		print line

def main():
	results=[]
	parser = argparse.ArgumentParser(usage="-h for full usage")
	parser.add_argument('query', help='search term')
	parser.add_argument('-c', dest="count", help='count number of occurrences')
	parser.add_argument('-v', dest="notfound", help="lines that doesn't contain query")
	parser.add_argument('-u', dest="up", help="update database")
	args = parser.parse_args()
	if args.up: update_db()
	else:
		if args.count: results.append(count(args.query))
		elif args.notfound: results=unfind(args.query)
		else:
			results=find(args.query)
		fprint(results)
main()