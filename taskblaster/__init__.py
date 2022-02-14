# This is a simple library which uses MPI4PY to run a bunch of tasks.

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def RunTasks(tasks):
    import gepy.executor as ge
    # work out which tasks are mine.
    stencil = []
    i = rank

    if (rank == 0):
        print("Decomposition:\n")

    comm.Barrier()

    while (i < len(tasks)):
        stencil.append(i)
        print(rank, ": ", tasks[i])
        i += size

    comm.Barrier()
    if (rank == 0):
        print("\nRunning tasks:\n")    
    comm.Barrier()

    for j in stencil:
        print(rank, ": ", tasks[j])
        status = ge.run(tasks[j])
        print(rank, ": ", tasks[j], "\n",
              rank, ": ", "Return code: ", status.returncode, "\n",
              rank, ": ", "Stdout: ", status.stdout, "\n",
              rank, ": ", "Stderr: ", status.stderr)
    comm.Barrier()

    if (rank == 0):
        print("\nFinished\n")    
