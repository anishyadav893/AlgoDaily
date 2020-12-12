# This is my solution for AlgoDaily problem Validate Palindrome
# Located at https://algodaily.com/challenges/validate-palindrome

def is_palindrome(s):
    s = s.replace(' ', '')
    s = s.lower()
    if s == s[::-1]:
      return True
    else:
      return False

# We can also achieve this with a while loop, starting from the first
# and last element and then incremnting and decrementing the values
# of the start and end variables respectively
'''
def reverse_str(str):
  start = 0
  end = len(str)-1
  str_copy = [letter for letter in str]
  while start < end:
    temp = str_copy[start]
    str_copy[start] = str_copy[end]
    str_copy[end] = temp
    start += 1
    end -= 1
  return "".join(str_copy)
'''