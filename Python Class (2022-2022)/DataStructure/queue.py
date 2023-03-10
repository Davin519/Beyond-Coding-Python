class Queue:
    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0


queue = Queue()
for _ in range(5):
    queue.push(input())

while not queue.isEmpty():
    print(queue.pop(), end='')