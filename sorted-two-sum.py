# This is my solution for AlgoDaily problem Sorted Two Sum
# Located at https://algodaily.com/challenges/sorted-two-sum

def sorted_two_sum(nums, goal):
    start = 0
    end = len(nums) - 1
    
    while start < end:
        if nums[start] + nums[end] == goal:
            return [start, end]
        elif nums[start] + nums[end] < goal:
            start += 1
        else:
            end -= 1
    return []