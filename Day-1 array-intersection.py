# This is my solution for AlgoDaily problem Array Intersection
# Located at https://algodaily.com/challenges/array-intersection

def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    
    return list(nums1.intersection(nums2))
    
    # Normal solution, not so optimized
    # kind of brute force
    '''empty = []
    if len(nums1) >= len(nums2):
      for i in nums2:
        if (i in nums1) and (i not in empty):
          empty.append(i)
    else:
      for i in nums1:
        if (i in nums2) and (i not in empty):
          empty.append(i)
    return empty'''