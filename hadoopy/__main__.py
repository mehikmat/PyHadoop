__author__ = 'hikmat'

"""
Module docstring.
This serves as a long usage message.
"""
__author__ = 'hikmat'

import argparse

def cmd():
	parser = argparse.ArgumentParser(description='Process some integers.')

	parser.add_argument('list', metavar='ls', type=string, nargs='+',
	                   help='lists hadoop file system')
	parser.add_argument('cat' help='reads top 10 lines of file in stored hdfs')

	args = parser.parse_args()

	print args.accumulate(args.integers)


def main():
    cmd()


if __name__ == '__main__':
    sys.exit(main())