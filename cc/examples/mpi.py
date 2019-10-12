#qsub mpi.qsub
def hello_world(n):
  import time
  time.sleep(1)
  return "Hello world "+str(n)

if __name__ == '__main__':
  from dask.distributed import Client, LocalCluster
  from dask_mpi import initialize
  import time
  import numpy as np 

  initialize(local_directory='/scratch/users/sapatha2/', nanny=False, dashboard=False)
  client = Client()
  
  res = client.map(hello_world, np.arange(380))
  start = time.time()
  for r in res: 
      print (r.result())
  client.close()
  print(time.time() - start)
  exit(0)
