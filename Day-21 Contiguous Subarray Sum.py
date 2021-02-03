def subarray_sum(nums, n):
    sums_map = dict()
    sum = 0

    for i in nums:
        sum += i
        if (sum - n) in sums_map:
            return True

        sums_map[sum] = True

    return False