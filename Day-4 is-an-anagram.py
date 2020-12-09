# This is my solution for AlgoDaily problem Is An Anagram
# Located at https://algodaily.com/challenges/is-an-anagram

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    return sorted(str1) == sorted(str2)


