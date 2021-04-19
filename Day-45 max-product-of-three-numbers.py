# This is my solution for AlgoDaily problem Max Product of Three Numbers
# Located at https://algodaily.com/challenges/max-product-of-three-numbers

def max_product_of_three(arr):
    arr = sorted(arr)
    prod1 = arr[-1] * arr[-2] * arr[-3]
    prod2 = arr[0] * arr[1] * arr[-1]
    
    if prod1 > prod2:
        return prod1
    return prod2