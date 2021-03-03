# This is my solution for AlgoDaily problem Implement a Linked List
# Located at https://algodaily.com/challenges/implement-a-linked-list

class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, newVal):
        current = self.head
        newNode = LinkedListNode(newVal)
        newNode.next = current
        self.head = newNode

        if not self.tail:
            self.tail = newNode

    def append(self, newVal):
        newNode = LinkedListNode(newVal)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def toString(self):
        toPrint = list()
        curr = self.head

        while curr:
            toPrint.append(curr.val)
            curr = curr.next

        return " -> ".join(str(x) for x in toPrint)