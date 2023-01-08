class Deque:
    def __init__(self):
        self.items = []
    
    def pushLeft(self, item):
        self.items.insert(0, item)
    
    def popRight(self):
        return self.items.pop()
    
    def peekRight(self):
        return self.items[-1]
    
    def pushRight(self, item):
        self.items.append(item)
    
    def popLeft(self):
        return self.items.pop(0)
    
    def peekLeft(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0


deque = Deque()
for _ in range(5):
    deque.pushLeft(input())

while not deque.isEmpty():
    print(deque.popLeft(), end=' ')