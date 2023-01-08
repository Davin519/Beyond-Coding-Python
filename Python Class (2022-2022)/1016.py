x = [1, 2, 3]

def addTen(n):
    return n+10

print(list(map(addTen, x)))

print(list(map(lambda x: x+10 ,x)))