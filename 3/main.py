# What is the largest prime factor of the number 600851475143

import sys
import math

def sieve_of_eratosthenes(n):
  prime_nums = [0]*(n-1)
  
  # construct list of numbers from 2 ... n
  for i in range(2, n+1):
    prime_nums[i-2] = i
 
  p = 2 # initialize p to smallest prime
  index = 1 # keeps track of next number to use as p
 
  while p < n - 1 and index < len(prime_nums) - 1:
    # remove multiples of p
    for num in prime_nums:
      if num % p == 0 and num != p:
        # print "prime is %d, removing %d" % (p, num)
        prime_nums.remove(num)
    # print "p: %d index: %d | " % (p, index)
    # print prime_nums
 
    p = prime_nums[index] # set p to next prime
    index += 1 # keeps track of kth prime
  return prime_nums

def get_prime_divisors(n):
  prime_divisors = []
  # divide n by primes up to sqrt(n)+1
  for i in sieve_of_eratosthenes(n):    
    # print "current prime: %d, n = %d" % (i, n)
    if n % i == 0: # found prime divisor
      prime_divisors.append(i)
      n /= i
    
    if i > math.sqrt(n) + 1: # no need to check further
      # print "breaking: %d > %d" % (i, math.sqrt(n)+1)
      break

  if n > 1: # if n is prime
    prime_divisors.append(n)
  return prime_divisors

def main(argv):
  print max(get_prime_divisors(int(argv[0])))
  sys.stdout.flush()

if __name__ == "__main__":
  main(sys.argv[1:])
