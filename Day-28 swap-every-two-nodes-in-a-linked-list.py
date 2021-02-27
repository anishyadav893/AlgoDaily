# This is my solution for AlgoDaily problem Swap Every Two Nodes in a Linked List
# Located at https://algodaily.com/challenges/swap-every-two-nodes-in-a-linked-list

def swap_every_two(head):
    if not head or not head.next:
        return None
      
    second_node = head.next
    third_node = second_node.next
    second_node.next = head

    head.next = swap_every_two(third_node)
    return second_node