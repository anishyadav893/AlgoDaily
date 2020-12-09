# This is my solution for AlgoDaily problem Fizz Buzz
# Located at https://algodaily.com/challenges/fizz-buzz

def fizz_buzz(n):
  empty = ''
  for i in range(1, n+1):
    if (i % 3 == 0) and (i % 5 != 0):
      empty += 'fizz'
    elif (i % 5 == 0) and (i % 3 != 0):
      empty += 'buzz'
    elif (i % 3 == 0) and (i % 5 == 0):
      empty += 'fizzbuzz'
    else:
      empty += str(i)
    
  return empty
