#!/usr/bin/python3

import sys

argv = sys.argv[1:]
num_args= len(argv)

if num_args == 0:
    print("0 argument.")
    print(".")
else:
    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")
    for i, arg in enumerate(agrv , 1):
        print(f"{i}: {arg}")
