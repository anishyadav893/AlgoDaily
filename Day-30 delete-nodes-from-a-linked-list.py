# This is my solution for AlgoDaily problem Delete Nodes From A Linked List
# Located at https://algodaily.com/challenges/delete-nodes-from-a-linked-list

# delete node given its key
def removeNodes(head, key):
    new_head = head
    temp = head

    if temp is not None:
        if temp.val == key:
            new_head = temp.next
            temp = None
            return new_head

    while temp is not None:
        if temp.val == key:
            break
        prev = temp
        temp = temp.next

    if temp is None:
        return new_head

    prev.next = temp.next
    temp = None
    return new_head