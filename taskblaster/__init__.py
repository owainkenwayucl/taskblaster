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
    while (i < len(tasks)):
        stencil.append(i)
        i += size

    for j in stencil:
        print(rank, " ", tasks[j])
        status = ge.run(tasks[j])
        print("Return code: ", status.returncode)
        print("Stdout: ", status.stdout)
        print("Stderr: ", status.stderr)

    comm.Barrier()
