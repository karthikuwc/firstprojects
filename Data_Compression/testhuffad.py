
from itertools import groupby
from camzip import camzip
from camunzip import camunzip
from filecmp import cmp
from os import stat
from json import load
import arithmeticac as arith
from math import log2
import time

filename = 'hamlet.txt'
method = 'iadhuffman'
p = {}
for i in range(128):
    p[i] = 1/128

camzip(method, filename, pr=p)
camunzip(filename + '.cz' + method[0], pr=p)



Nin = stat(filename).st_size
print(f'Length of original file: {Nin} bytes')
Nout = stat(filename + '.cz' + method[0]).st_size
sha = 8.0*Nout/Nin
print(f'Length of compressed file: {Nout} bytes')
print(f'Compression rate: {8.0*Nout/Nin} bits/byte')
if cmp(filename,filename+'.cuz'):
    print('The two files are the same')
else:
    print('The files are different')