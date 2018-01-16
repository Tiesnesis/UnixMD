#!/usr/bin/env python

from mpi4py import MPI
import sys

import itertools
import hashlib
import textwrap
import math
import time

startTime = time.time()

collection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# "U"
hashToFind = "4c614360da93c0a041b22e537de151eb"

comm = MPI.COMM_WORLD
processCount = comm.Get_size()
processRank = comm.Get_rank()
processName = MPI.Get_processor_name()

if processRank == 0:
    partList = textwrap.wrap(collection, int(math.ceil(len(collection)/float(processCount-1))))
    print "Collection divided according to process count:", partList
    # Add part for Rank 0, which is not invovled in calculations
    partList.insert(0, '')
else:
    partList = None
# Distribute parts to all Ranks
partList = comm.scatter(partList, root=0)

# If rank is not root rank, start the calculation
if processRank != 0:
    print "Process Rank:", processRank, " With name:", processName, " received part:",partList
    isFound = False
    # Array where combinations for each char will be stored
    arrayForCharCombinations = [partList]
    while not isFound:
        # Generate all possible combinations and loop them
        for tryArray in itertools.product(*arrayForCharCombinations):
            tryString = ''.join(tryArray)
            # Check if other Rank hasn't calculated solution already
            if comm.Iprobe(source=0, tag=11):
                isFound = True
                break
            # Generate hash for current combination
            tryHashed = hashlib.md5(tryString).hexdigest()
            # If current combination hash is correct, send this info to Rank 0
            if tryHashed == hashToFind:
                comm.send(tryString, dest=0, tag=11)
                # Tag that solution has been found
                isFound = True
                break
        # If code is getting this far, solution is not found, this will add another combination for next char
        arrayForCharCombinations.append(collection)
# Rank 0 validates if solution has been found
else:
    # Solution has been found if this kind of info received from other Ranks
    received = comm.recv(source=MPI.ANY_SOURCE, tag=11)
    # Rank 0 sending all ranks flag that solution has been found
    for process in range(1, processCount):
        print "Killing process:", process
        comm.send(received, dest=process, tag=11)
    endTime = time.time()
    print "Solution was:",received," found in:", (endTime - startTime), " seconds ---"
