# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:30:14 2019

@author: jkannenberg
"""


import argparse

from export_batch_events import export_batch_events

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--number_of_orders', default=10, type=int)
    parser.add_argument('--batch_size', default=5, type=int)
    parser.add_argument('--interval', default=1, type=int)
    parser.add_argument('--output_directory')

    args = parser.parse_args()

    number_of_loops = args.number_of_orders/ args.batch_size 

    i=0
    while i < number_of_loops:
        export_batch_events(args.batch_size, args.interval, args.output_directory).export_json()
        i += 1



if __name__ == '__main__':

    main()
    