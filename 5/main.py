# We want the smallest positive integer that is evenly
# divisble by all the positive integers from 1 to 20

# very brute force, but should work

import sys

def perfectly_divisible(n):
  for i in range(2, 21):
    if n % i != 0:
      return False
  return True

def smallest_divisible_by_nine_primes(n):
  while not perfectly_divisible(n):
    n = n + 1
  return n

def main(argv):
  print smallest_divisible_by_nine_primes(1)
  sys.stdout.flush()

if __name__ == "__main__":
  main(sys.argv[1:])
