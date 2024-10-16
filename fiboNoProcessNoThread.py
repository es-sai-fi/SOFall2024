from fibonacci import fibo
from time import time

def main():
  max_fibo = 33
  vector = [max_fibo]*12
  ts = time() 
  for x in range(12):
    vector[x] = fibo(x)

  print(f"Tomo {time() - ts}")

if __name__ == "__main__":
  main()
