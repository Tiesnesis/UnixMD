pip install -r requirements.txt
source env/bin/activate
mpiexec -n 2 --hostfile localhost python main.py
mpiexec -n 3 --hostfile localhost python main.py
mpiexec -n 5 --hostfile localhost python main.py
mpiexec -n 9 --hostfile localhost python main.py
mpiexec -n 13 --hostfile localhost python main.py
deactivate
