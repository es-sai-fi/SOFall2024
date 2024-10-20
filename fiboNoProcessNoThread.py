from fibonacci import fibo
from time import time

def main():
  vector = [33]*144
  ts = time() 
  for x in range(144):
    vector[x] = fibo(vector[x])
  print(f"Tomó {time() - ts}")
  print(vector)
if __name__ == "__main__":
  main()
