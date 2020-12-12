# This is my solution for AlgoDaily problem Single Lonely Number
# Located at https://algodaily.com/challenges/lonely-number

def lonely_number(numbers):
    empty = {}
    
    for i in numbers:
      empty[i] = numbers.count(i)
      if empty[i] == 1:
        return i
  
  # The code below also uses a dictionary but deletes the initial entry
  # if an element shows up twice effectively keeping only the
  # lonely number in our dictionary
  '''appearances = {}

    for num in numbers:
        if num in appearances:
            del appearances[num]
        else:
            appearances[num] = True

    return appearances.keys()[0]'''


