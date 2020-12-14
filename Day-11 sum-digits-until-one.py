# This is my solution for AlgoDaily problem Sum Digits Until One
# Located at https://algodaily.com/challenges/sum-digits-until-one

#import functools


def sum_digits(num):
  num = str(num)
  
  while len(num) != 1:
    total = 0
    for i in num:
      total += int(i)
    num = str(total)
      
  return int(num)

# a much easier way but not that intuitive is to simply
# return num % 9
# and we will get our answer
    

