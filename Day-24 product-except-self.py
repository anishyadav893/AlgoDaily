# This is my solution for AlgoDaily problem Product Except Self
# Located at https://algodaily.com/challenges/product-except-self

import math

def product_except_self(nums):
    product_all = math.prod(nums)
    answer = []
    
    for i in nums:
        answer.append(product_all / i)
        
    return answer