# This is my solution for AlgoDaily problem Missing Number In Unsorted
# Located at https://algodaily.com/challenges/missing-number-in-unsorted

def missing_in_unsorted(arr, lowerBound, upperBound):
    for i in range(lowerBound, upperBound + 1):
      if i not in arr:
        return i
      
'''
Another way of solving this problem is to take the sum of the integers till the upper bound
then subtract from it the sum of integers till the lower bound.
Now, whatever sum you get you just have to subtract from it the sum of integers in the array.
Whatever result you'll get will be our final answer.
'''