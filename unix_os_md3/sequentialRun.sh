pip install -r requirements.txt
source env/bin/activate
mpiexec -n 2 --hostfile localhost python main.py $1
mpiexec -n 3 --hostfile localhost python main.py $1
mpiexec -n 5 --hostfile localhost python main.py $1
mpiexec -n 9 --hostfile localhost python main.py $1
mpiexec -n 11 --hostfile localhost python main.py $1
deactivate
