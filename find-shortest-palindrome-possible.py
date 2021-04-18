# This is my solution for AlgoDaily problem Find Shortest Palindrome Possible
# Located at https://algodaily.com/challenges/find-shortest-palindrome-possible

def shortestPalindrome(s):
    start = 0
    end = len(s) - 1
    
    for i in range(end, -1, -1):
        if s[start] == s[i]:
            start += 1
    
    if start == len(s):
        return s
    
    palindromeEnd = s[start:]

    return (
        "".join(list(palindromeEnd)[::-1]) + shortestPalindrome(s[0:start]) + palindromeEnd
    )