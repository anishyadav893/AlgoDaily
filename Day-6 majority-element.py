# This is my solution for AlgoDaily problem Majority Element
# Located at https://algodaily.com/challenges/majority-element

###
# @param {number[]} nums
# @return {number}
###
from math import floor
from collections import Counter

def majority_element(nums):
    nums.sort()
    return nums[int(floor(len(nums) / 2))]
    

# print(majorityElement([1, 1, 1, 4, 2, 4, 4, 3, 1, 1, 1]))

# from collections import Counter
		'''countDict = Counter(nums)
    mostCommon = countDict.most_common()
    print(mostCommon[0][0])'''
