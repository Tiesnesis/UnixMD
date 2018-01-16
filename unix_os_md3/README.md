# Calculate hash for string using python and MPI
## Requirements
- install python 2.7
- install pip

## Running MPI example

It is possible to run this MPI example in two ways:
 - `mpiexec -n <Threads+1> --hostfile localhost python main.py <StringToFind>` - will run one calculation with specified thread count
 - `sh sequentialRun.sh` - will run 5 calculations with thread count: 1,2,4,8,11
