# This is my solution for AlgoDaily problem Targets and Vicinities
# Located at https://algodaily.com/challenges/targets-and-vicinities

def getTV(actual, guess):
    actual = str(actual)
    guess = str(guess)
    
    target = 0
    vicinity = 0
    
    num = [0] * 10

    for i in range(len(str(guess))):
        if actual[i] == guess[i]:
            target += 1
        else:
            if num[int(actual[i])] < 0:
                vicinity += 1
            if num[int(guess[i])] > 0:
                vicinity += 1
            num[int(actual[i])] += 1
            num[int(guess[i])] -= 1
    return "{}T{}V".format(target, vicinity)