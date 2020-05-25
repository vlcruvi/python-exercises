#!/usr/bin/env python3

import sys

def checking(words):
    for i in words:
        reversed_word = i[len(i)::-1].lower().split()
        i = i.lower().split()
        if reversed_word == i:
            print ("True")
        else:
            print ("False")

def main():
    filename = sys.argv[1]
    f = open(filename, 'r')

    checking(f)

main()
