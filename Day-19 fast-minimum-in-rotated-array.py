# This is my solution for AlgoDaily problem Fast Minimum In Rotated Array
# Located at https://algodaily.com/challenges/fast-minimum-in-rotated-array

def get_minimum(nums):
    for i in range(len(nums) - 1):
      if nums[i] > nums[i+1]:
        nums = nums[i+1:] + nums[:i+1]
        return nums[0]