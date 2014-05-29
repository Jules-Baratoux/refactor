#!/usr/bin/env python3
from os import rename
from os.path import basename, dirname, join, isfile
from re import sub

from args import Args

class Refactor:

	def __init__(self, pattern, repl):
		self.pattern = pattern
		self.repl    = repl

	def replace(self, string):
		return sub(self.pattern, self.repl, string)

	def replace_content(self, pathname):

		with open(pathname, 'r') as R:
			content = R.read()

		with open(pathname, 'w') as W:
			W.write(self.replace(content))

	def replace_filename(self, pathname):
		rename(pathname, join(dirname(pathname), self.replace(basename(pathname))))



if __name__ == '__main__':
	args = Args()

	refactor = Refactor(args.pattern, args.replace)

	for pathname in args.pathnames:
		print(pathname)
		if isfile(pathname):
			refactor.replace_content(pathname)
		refactor.replace_filename(pathname)
