#python local.py
def hello_world(n):
  import time
  time.sleep(1)
  return "Hello world "+str(n)

if __name__ == '__main__':
  from dask.distributed import Client, LocalCluster
  import time
  import numpy as np 

  cluster = LocalCluster(n_workers = 4, threads_per_worker = 1)
  client = Client(cluster)
  
  print(cluster)
  print(client.nthreads())

  start = time.time()
  res = client.map(hello_world, np.arange(36))
  for r in res:
    print(r.result())
  
  client.close()
  print(time.time() - start)
