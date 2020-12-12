# This is my solution for AlgoDaily problem Power of Three
# Located at https://algodaily.com/challenges/power-of-three

def power_of_three(num):
    if num == 1:
      return True
    
    while num > 0:
      num = num / 3
      if num == 1:
        return True
    
    return False


