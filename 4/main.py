import sys

def num_digits(n):
  num = 1
  n = int(abs(n))
  if n >= 100000000:
    n /= 100000000
    num += 8
  if n >= 10000:
    n /= 10000
    num += 4
  if n >= 100:
    n /= 100
    num += 2
  if n >= 10:
    n /= 10
    num += 1
  return num

def is_palindrome(num):
  n_digits = num_digits(num)  
  num_copy = num

  if n_digits == 1: return True

  offset = 10.0 ** (n_digits - 1)
  reversed = 0
  
  for i in range(1, n_digits + 1):
    temp = num_copy % (10 ** i)
    reversed += temp * offset
    num_copy -= temp
    offset /= 100
  
  if reversed == num:
    return True
  else:
    return False

def largest_palindrome(num_digits):
  max = 0
  for i in range(1, 10**num_digits):
    for j in range(1, 10**num_digits):
      curr = i * j
      if curr > max and is_palindrome(curr):
        max = curr

  return max

def main(argv):
  print largest_palindrome(int(argv[0]))

if __name__ == "__main__":
  main(sys.argv[1:])
