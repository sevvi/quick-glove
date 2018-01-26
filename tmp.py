from __future__ import print_function

import itertools
import os
import struct
import sys

import tensorflow as tf

from six.moves import xrange



with open("cooccurrence.bin", 'rb') as coocs:

    glove_cooc_fmt = struct.Struct('iid')

    coocs.seek(0, os.SEEK_END)
    ncoocs = coocs.tell() / glove_cooc_fmt.size
    coocs.seek(0, os.SEEK_SET)


    for ix in xrange(ncoocs):
         bits = coocs.read(glove_cooc_fmt.size)
         row_id, col_id, cnt = glove_cooc_fmt.unpack(bits)
         print(row_id, col_id, cnt)
