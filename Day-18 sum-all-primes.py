# This is my solution for AlgoDaily problem Sum All Primes
# Located at https://algodaily.com/challenges/sum-all-primes

def sumOfPrimes(n):
    sumPrimes = 0
    for i in range(2, n+1):
      if isPrime(i):
        sumPrimes += i
    return sumPrimes
  
def isPrime(num):
    for i in range(2, int(num/2) + 1):
      if num % i == 0:
        return False
    return True