# MPI-Python
A little Python script using MPI. An array is defined in one process, then its elements are equally distributed between all processes which sum the elements and return the result to the source.

To run, use: mpiexec -n X python mpi3.py
-X is the number of processes to be used
