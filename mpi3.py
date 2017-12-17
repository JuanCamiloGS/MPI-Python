#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 08:51:53 2017

@author: juan
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    array = np.asarray([x for x in range(size*3)])
    print "array: ", array
    data = np.array_split(array,size,axis=0)
else:
    data = None

data = comm.scatter(data, root=0)
print("{} from node {}".format(data, rank))
sumarray = np.sum(data)
res = comm.gather(sumarray, root=0)

if rank == 0:
   print 'master:', res