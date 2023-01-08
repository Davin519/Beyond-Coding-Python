# def yee(x):
#     c=0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             c+=1
#     return c

# def yeet(y): 
#     i = yee(y)
#     if i == 2:
#         print("prime")
#     else:
#         print("composite")

# n = int(input())

# yeet(n)

# class Person:
#     def __init__(self,heart, eyes):
#         self.heart = heart
#         self.eyes = eyes

#     def hello(self, name):
#         print(f"Hello~ {name}")
    
# class ProGamer(Person):
#     def gaming(self, game):
#         print(f"playing {game}")

# Camman18 = ProGamer(1, 2)
# print(Camman18.eyes)

# x = ""   
# with open("a.txt", "r") as f:
#     x = f.read()
# with open("b.txt", "w") as f:
#     f.write(x)

def copyPaste(fname1, fname2):
    with open(fname1, "r") as f1, open(fname2, "w") as f2:
        f2.write(f1.read())

copyPaste("a.txt", "b.txt")