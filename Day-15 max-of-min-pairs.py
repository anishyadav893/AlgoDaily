# This is my solution for AlgoDaily problem Max of Min Pairs
# Located at https://algodaily.com/challenges/max-of-min-pairs

def max_of_min_pairs(nums):
    nums = sorted(nums)
    answer = 0
    
    for i in range(0, len(nums) - 1, 2):
      if nums[i] < 0 and (nums[i+1] > 0):
        answer += nums[i+1]
      else:
        answer += nums[i]
      
    return answer
  
  '''
  As the time complexity is n(log(n)), we first sort the list and add the elements at every 2nd
  position to the 'answer' variable we created.
  Remember to take care of the negative integers as well and when there is a positive and a negative
  integer in the pair. 
  '''
  
  #NOTE - for this particular question, the test cases contain all positive integers only.