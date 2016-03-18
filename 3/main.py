# What is the largest prime factor of the number 600851475143

from bitarray import bitarray
import sys
import math

def sieve_of_eratosthenes(n):
  if n == 2:
    return [2]
  
  prime_nums = bitarray(n-1)
  prime_nums.setall(False)
  
  p = 2 # initialize p to smallest prime
   
  while p < n:
    # put a 1 in indexes that are multiples of p
    for i in range(p + 1, n + 1):
      if i % p == 0:
        prime_nums[i-2] = bitarray('1')

    if prime_nums[n-2] == 1:
      break

    # set p to next prime
    for i in range(p + 1, n + 1):
      if prime_nums[i-2] == 0:
        p = i
        break

  ans = []
  for i in range(0, n-1):
    if prime_nums[i] == 0:
      ans.append(i+2)
  return ans

def get_prime_divisors(n):
  prime_divisors = []
  # divide n by primes up to sqrt(n)+1
  for i in sieve_of_eratosthenes(int(math.sqrt(n))):    
    if n % i == 0: # found prime divisor
      prime_divisors.append(i)
      n /= i    

  return prime_divisors

def main(argv):
  print max(get_prime_divisors(int(argv[0])))
  sys.stdout.flush()

if __name__ == "__main__":
  main(sys.argv[1:])
