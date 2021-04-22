# This is my solution for AlgoDaily problem Split Set to Equal Subsets
# Located at https://algodaily.com/challenges/split-set-to-equal-subsets

def has_equal_subsets(nums):
    s = sum(nums)
    if s % 2 != 0:
        return False
    
    memo = [[-1 for x in range(int(s / 2) + 1)] for y in range(len(nums))]
    if has_equal_subsets_helper(memo, nums, int(s / 2), 0) == 1:
        return True
    else:
        return False

def has_equal_subsets_helper(memo, nums, summation, curr_idx):
    if summation == 0:
        return 1

    n = len(nums)
    if n == 0 or curr_idx >= n:
        return 0

    if memo[curr_idx][summation] == -1:
        if nums[curr_idx] <= summation:
            if (
                has_equal_subsets_helper(memo, nums, summation - nums[curr_idx], curr_idx + 1)
                == 1
            ):
                memo[curr_idx][summation] = 1
                return 1
        memo[curr_idx][summation] = has_equal_subsets_helper(memo, nums, summation, curr_idx + 1)

    return memo[curr_idx][summation]