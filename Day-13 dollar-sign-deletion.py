# This is my solution for AlgoDaily problem Dollar Sign Deletion
# Located at https://algodaily.com/challenges/dollar-sign-deletion

def is_dollar_delete_equal(arr):
    str1 = list()
    str2 = list()
    
    for i in arr[0]:
      if i == "$" and len(str1) > 0:
        str1.pop()
      elif i != "$":
        str1.append(i)
        
    for j in arr[1]:
      if j == "$" and len(str2) > 0:
        str2.pop()
      elif j != "$":
        str2.append(j)
        
    return ''.join(str1) == ''.join(str2)
  
  '''
  Just initialize two empty lists and keep on adding to the list and if there is a dollar sign
  then pop the last element from your new list and skip the dollar sign. Do it with both lists,
  join them and finally compare and return the result.
  '''