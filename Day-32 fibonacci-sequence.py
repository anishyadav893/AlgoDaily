# This is my solution for AlgoDaily problem Fibonacci Sequence
# Located at https://algodaily.com/challenges/fibonacci-sequence

##
# @param {number} n The Fibonacci number to get.
# @returns {number} The nth Fibonacci number
##

memo = {}


def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)