#! /usr/bin/env python3
# coding: utf-8

import logging as log
import argparse
import analysis.csv as c_an
import analysis.xml as x_an
import matplotlib
matplotlib.use('TkAgg')

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?""")
    parser.add_argument("-d","--datafile",help="""CSV or XML file containing pieces of information about the members of parliament""")
    parser.add_argument("-v", "--verbose", action='store_true', help="""Make the application talk!""")
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.verbose:
        log.basicConfig(level=log.DEBUG)
    try:
        datafile = args.datafile
        if datafile == None:
            raise Warning('You must indicate a datafile!')
        else:
            try:
                if args.extension == 'xml':
                    x_an.launch_analysis(datafile)
                elif args.extension == 'csv':
                    c_an.launch_analysis(datafile)
            except FileNotFoundError as e:
                log.warning("The file was not found. Here is the original message of the exception :" + e)
            finally:
                log.info('#################### Analysis is over ######################')
    except Warning as e:
        print(e)

if __name__ == "__main__":
    main()