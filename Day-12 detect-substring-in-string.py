# This is my solution for AlgoDaily problem Detect Substring in String
# Located at https://algodaily.com/challenges/detect-substring-in-string

def detectSubstring(txt, subStr):
    for i in range(0, (len(txt) - len(subStr) + 1)):
      if txt[i:(i + len(subStr))] == subStr:
        return i
    return -1


