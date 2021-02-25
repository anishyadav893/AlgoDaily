# This is my solution for AlgoDaily problem Two Sum
# Located at https://algodaily.com/challenges/two-sum

def two_sum(nums, goal):
    empty = dict()
    
    for idx, val in enumerate(nums):
        second_num = goal - val
        if second_num not in empty:
            empty[val] = idx
        else:
            return [empty[second_num], idx]
          
    return []