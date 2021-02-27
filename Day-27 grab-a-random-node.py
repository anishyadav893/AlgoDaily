# This is my solution for AlgoDaily problem Grab a Random Node
# Located at https://algodaily.com/challenges/grab-a-random-node

import random
import math


def fetch_random_node(head):
    node_array = list()
    current = head
    
    while current:
        node_array.append(current.val)
        current = current.next
        
    number = math.floor(random.random() * len(node_array))
    
    while number >= 0 and head and head.next:
        head = head.next
        number -= 1
        
    return head.val