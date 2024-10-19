from fibonacci import fibo
from time import time
import multiprocessing
import sys

vector = [33]*144

class FiboWorker(multiprocessing.Process):
  def __init__(self, n):
    multiprocessing.Process.__init__(self)
    self.n = n

  def run(self):
    start = self.n*12
    end = start+12
    for x in range(start, end):
      vector[x] = fibo(vector[x]) 


def main():
  procesos = []
  ts = time() 
  for x in range(12): 
    worker = FiboWorker(x)
    worker.start()
    procesos.append(worker)

  for worker in procesos: 
    worker.join()

  print(f"Tomó {time() - ts}")


if __name__ == "__main__":
  main()
