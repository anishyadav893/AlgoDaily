# This is my solution for AlgoDaily problem Reverse Only Alphabetical
# Located at https://algodaily.com/challenges/reverse-only-alphabetical

import re


def reverse_only_alpha(s):
    temp = []
    empty = ''
    
    regex = re.compile('[a-zA-Z]')
    
    for letter in s:
      if regex.match(letter):
        temp.append(letter)
    
    temp = reverse_array(temp)
    
    counter = 0
    for i in range(len(s)):
      if regex.match(s[i]):
        empty += temp[counter]
        counter += 1
      else:
        empty += s[i]
    
    return empty


def reverse_array(arr):
    return arr[::-1]


