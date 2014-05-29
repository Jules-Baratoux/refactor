#!/usr/bin/env python3
from sys import argv
from os.path import basename

class Args:

	name  = basename(argv[0])
	usage = '[--python] PATTERN [--python] REPLACE PATHNAME [PATHNAMES ...]'

	def __init__(self):
		n = 1

		def args(n):
			try:
				return argv[n]
			except IndexError:
				print ('usage:', Args.name, Args.usage)
				exit()

		def _eval(expression):
			try:
				return eval(expression, {})
			except Exception as exception:
				print(Args.name+':', '‘'+expression+'’', 'raised an exception:')
				print(exception.__class__.__name__ +':', exception)
				exit()

		def expression(n):
			option = args(n)
			if option == '-p' or option == '--python':
				expression = args(n+1)
				return n+2, _eval(expression)
			else:
				return n+1, option

		n, self.pattern = expression(n);
		n, self.replace = expression(n);
		self.pathnames  = argv[n:]

if __name__ == '__main__':
	args = Args()
