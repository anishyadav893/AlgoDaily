# This is my solution for AlgoDaily problem How Out of Order
# Located at https://algodaily.com/challenges/how-out-of-order

def inversions(l):
     return finalMerge(l, 0, len(l) - 1)

def finalMerge(arr, start, end):
    inv_count = 0
    
    if start < end:
        mid = (start + end) // 2
        
        inv_count += finalMerge(arr, start, mid)
        inv_count += finalMerge(arr, mid + 1, end)
        inv_count += invert(arr, start, mid, end)
    
    return inv_count
  
def invert(arr, start, mid, end):
    i = start
    j = mid + 1
    count = 0
    
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            i += 1
        else:
            count += mid - i + 1
            j += 1
    return count