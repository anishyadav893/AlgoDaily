# This is my solution for AlgoDaily problem Find First Non-Repeating Character
# Located at https://algodaily.com/challenges/find-first-non-repeating-character

from collections import OrderedDict

def first_non_repeat(s):
    word_count = OrderedDict()
    
    for letter in s:
      if letter not in word_count:
        word_count[letter] = 1
      else:
        word_count[letter] += 1
        
    for item in word_count:
      if word_count[item] == 1:
        return item
      
    return ""
  
'''
In this we have made use of the ordered dictionary module (a Python built-in function) to store the
individual letters as keys and their occurences as the values.
Then we iterate through in the created dictionary and as soon as the key with an occurence value of 1
is reached we return that value as our final answer.
'''