# This is my solution for AlgoDaily problem Union of Linked Lists
# Located at https://algodaily.com/challenges/union-of-linked-lists

def get_union(l1, l2):
    result = []
    n1 = l1
    n2 = l2
    
    while n1:
        result.append(n1.val)
        n1 = n1.next

    while n2:
        if present_in_l2(l1, n2.val):
            result.append(n2.val)
        n2 = n2.next

    return result


def present_in_l2(head, val):
    temp = head
    while temp:
        if temp.val == val:
            return False
        temp = temp.next

    return True