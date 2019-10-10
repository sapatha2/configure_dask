#qsub mpi.qsub
def hello_world(n):
  import time
  time.sleep(1)
  return "Hello world "+str(n)

if __name__ == '__main__':
  from dask.distributed import Client
  from dask_mpi import initialize
  import time
  import numpy as np 

  initialize()
  client = Client()
  
  start = time.time()
  res = client.map(hello_world, np.arange(180))
  for r in res: r.result()
  client.close()
  print(time.time() - start)
  
