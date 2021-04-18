# This is my solution for AlgoDaily problem Is A Subsequence
# Located at https://algodaily.com/challenges/is-a-subsequence

def is_a_subsequence(sub, string):
    if string.find(sub) == -1:
        return False
    return True