# This is my solution for AlgoDaily problem Find Missing Number in Array
# Located at https://algodaily.com/challenges/find-missing-number-in-array

def missing_numbers(num_arr):
    missing = []
    for i in range((num_arr[0] + 1), (num_arr[-1] + 1)):
      if i not in num_arr:
        missing.append(i)
    return missing
  
'''
We just iterate through the list once based on the first and last element's index.
We can do this since our array is supposed to be in a sequential order.
So whatever consecutive number isn't in the array, we add it to the missing array and return missing
at the end as our result.
'''