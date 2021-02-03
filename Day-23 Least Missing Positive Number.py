def least_missing_pos(nums):
    for i in range(len(nums)):
        while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
            swap(nums, i, nums[i] - 1)

    for j in range(len(nums)):
        if nums[j] != j + 1:
            return j + 1

    return len(nums) + 1


def swap(arr, first_idx, sec_idx):
    temp = arr[first_idx]
    arr[first_idx] = arr[sec_idx]
    arr[sec_idx] = temp