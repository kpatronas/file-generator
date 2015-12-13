#!/usr/bin/env python
import os
import sys
import uuid
import timeit
from datetime import datetime
import string
import random
import argparse

class FileGen:

    def __init__(self):

        self.units = {'b':1,                 # 1 Byte
                      'k':1024,              # 1 KB: 1024 bytes
                      'm':1024*1024,         # 1 MB: 1024 * 1024 bytes
                      'g':1024*1024*1024}    # 1 GB: 1024 * 1024 * 1024 bytes

        self.parser = argparse.ArgumentParser(description='Create binary files')
        
        self.parser.add_argument('-n', '--number',
            help = 'Number of files to generate',
            type = int,
            required = True)

        self.parser.add_argument('-s',
            '--size',
            help = 'Size (raw number)',
            type = int,
            required = True)

        self.parser.add_argument('-u',
            '--units',
            help = 'Units (bytes,kilobyte,megabyte,gigabyte)',
            required = True,
            choices=['b', 'k', 'm', 'g'])

        self.parser.add_argument('-e',
            '--extension',
            help = 'extension of the generated files',
            required = False)

        self.args = vars(self.parser.parse_args())
    
        if int(self.args['size']) <= 0:
            self.parser.error("Size cannot be equal or smaller than 0")

        if int(self.args['number']) <= 0:
            self.parser.error("Number of files cannot be equal or smaller than 0")

        self.size_kb = int(self.args['size']) * int(self.units[self.args['units']])

        operation_start = timeit.default_timer()
        for i in range(1,self.args['number']+1):
            file_start = timeit.default_timer()
            self.binary()
            file_stop = timeit.default_timer()
            msg = "Files created: %d/%d Avg time to create file: %f"%(i,self.args['number'],file_stop-file_start)
            print msg
        operation_stop = timeit.default_timer()
        print "Total time: %f"%(operation_stop-operation_start)

    def binary(self):
        self.ext = "bin" or self.args['extension']
        with open(str(uuid.uuid4())+"."+self.ext, 'wb') as fout:
            fout.write(os.urandom(self.size_kb))
            fout.close()

if __name__ == '__main__':
    FileGenerator = FileGen()
