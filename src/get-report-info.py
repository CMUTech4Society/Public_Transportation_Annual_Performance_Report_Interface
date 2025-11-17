#!/bin/env python
import argparse
from sys import argv
from preprocess import preprocess

def get_parser():
    parser = argparse.ArgumentParser() #formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('x_axis', action='store', metavar='<x-axis>',
                        help=("The dataset to map on the x-axis."))
    parser.add_argument('y_axis', action='store', metavar='<y-axis>',
                        help=("The dataset to map on the y-axis."))
    parser.add_argument('-y', '--y-filter', action='store', nargs='*',
                        metavar='y-axis filter',
                        help=('Filter(s) to apply to the y-axis. Each filter '
                              'should consist of a key, operator, and value, '
                              'in the form: <key> <operator> <value>. '
                              'Multiple filters can be appended with multiple '
                              'flags. See examples below.'))
    parser.add_argument('-x', '--x-filter', action='store', nargs='*',
                        metavar='x-axis filter',
                        help=('Filter(s) to apply to the x-axis, see '
                              '--y-filter above and the examples below.'))

    parser.add_argument('-m', '--multiplier', action='store',
                        help=('A multiplier to apply to the x-axis, in the '
                              'form <x/y> <operator> <key>.'))
    parser.add_argument('-t', '--tags', action='store', nargs='*')

    return parser;

def main():
    parser = get_parser()
    args = parser.parse_args(argv[1:])
    query = preprocess(args)
    
if __name__ == '__main__':
    main()
