#!/usr/bin/env python

from sys import stdout

class Utility:
    
    def printf(text, *args):
       "Write the arguments to stdout in the specified format."
       s = text % args
       stdout.write(s)
    
        
    def fprintf(file, text, *args):
        "Write the arguments to the given open file handle in the specified format"
        s = text * args
        file.write(s)
        
        
    def sprintf(text, *args):
        s = text % args
        return s

