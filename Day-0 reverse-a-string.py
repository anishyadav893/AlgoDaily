# This is my solution for AlgoDaily problem Reverse a String
# Located at https://algodaily.com/challenges/reverse-a-string

def reverse_string(str1):
    p1 = 0
    p2 = len(str1) - 1
    stringList = list(str1)
    
    while p1 < p2:
      temp = stringList[p1]
      stringList[p1] = stringList[p2]
      stringList[p2] = temp
      p1 += 1
      p2 -= 1
      
    return ''.join(stringList)
    
    # return str1[::-1]