# This is my solution for AlgoDaily problem Find the Intersection of Two Linked Lists
# Located at https://algodaily.com/challenges/find-the-intersection-of-two-linked-lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def getIntersection(list1, list2):
    if not list1 or not list2:
        return None
      
    p1 = list1
    p2 = list2
    
    list3 = []
    
    while (p1):
        while (p2):
            if (p1.val == p2.val):
                list3.append(p1.val)
                
            p2 = p2.next
        p1 = p1.next
        
    linked3 = Node(list3[0]
    create_nodes(linked3, list3[1:])
    return linked3