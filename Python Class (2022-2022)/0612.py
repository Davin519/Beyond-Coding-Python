# class Stack:
#     def __init__(self):
#         self.x = []

#     def push(self, a):
#         self.x.append(a)

#     def pop(self):
#         if self.empty():
#             print("list is empty")
#         self.x.pop()

#     def top(self):
#         if self.empty():
#             print("list is empty")
#         return self.x[-1]

#     def bottom(self):
#         if self.empty():
#             print("list is empty")
#         return self.x[0]

#     def empty(self):
#         return not bool(len(self.x))

# stack = Stack()
# stack.push(100)
# stack.bottom()
