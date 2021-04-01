# This is my solution for AlgoDaily problem Two Stack Queue
# Located at https://algodaily.com/challenges/two-stack-queue

class TwoStackQueue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def push(self, val):
        while len(self.inbox) != 0:
            self.outbox.append(self.inbox[-1])
            self.inbox.pop()
            
        self.inbox.append(val)
        
        while len(self.outbox) != 0:
            self.inbox.append(self.outbox[-1])
            self.outbox.pop()
            
        return

    def pop(self):
        if len(self.inbox) == 0:
            print("The Q is empty !!")
        
        top_val = self.inbox[-1]
        self.inbox.pop()
        return top_val