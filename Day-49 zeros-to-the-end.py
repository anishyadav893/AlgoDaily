# This is my solution for AlgoDaily problem Zeros to the End
# Located at https://algodaily.com/challenges/zeros-to-the-end

def zeros_to_the_end(nums):
    answer = []
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            count += 1
            answer.append(nums[i])
    
    remaining = len(nums) - count
    for i in range(remaining):
        answer.append(0)
    return answer

print(zeros_to_the_end([1, 0, 2, 0, 4, 0]))

def zeros_to_the_end(nums):
    insert_pos = 0
    for n in range(len(nums)):
        if nums[n] != 0:
            nums[insert_pos] = nums[n]
            insert_pos += 1

    for j in range(insert_pos, len(nums)):
        nums[j] = 0

    return nums