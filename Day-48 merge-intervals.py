# This is my solution for AlgoDaily problem Merge Intervals
# Located at https://algodaily.com/challenges/merge-intervals

def merge_intervals(ranges):
    if not ranges:
      return None
    
    if len(ranges) < 2:
      return ranges
    
    result = []
    ranges.sort(key = lambda x: x[0])
    
    last = ranges[0]
    
    for r in ranges:
      if r[0] <= last[1]:
          last = [last[0], max(r[1], last[1])]
      else:
          result.append(last)
          last = r
    
    result.append(last)
    return result
  
merge_intervals([[1, 4], [2, 5], [7, 10], [12, 16]])




