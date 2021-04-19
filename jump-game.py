# This is my solution for AlgoDaily problem Max Leaps in Jump Game
# Located at https://algodaily.com/challenges/jump-game

def max_leaps(nums):
  i = 0
  span = 0
  
  while i < len(nums) and i <= span:
    span = max(i + nums[i], span)
    i += 1
    
  return i == len(nums)