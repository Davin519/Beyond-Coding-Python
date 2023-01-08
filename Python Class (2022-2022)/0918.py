# import math
# x = int(input())
# c = 0
# for i in range(2, int(math.sqrt(x)) + 1):
#     if x % i == 0:
#         c+=1

# if c == 0:
#     print(True)
# else:
#     print(False)









# def lcm(x, y):


#    while(True):
#        if((f % x == 0) or (f % y == 0)):
#            lcm = f
#            break
#        f += 1

#    return lcm

# l = int(input())
# for i in range(0, l): 
#     b, a = map(int, input().split())
#     print(lcm(a, b))

def gcf(a, b):
  while (b != 0):
    t = a % b
    a = b
    b = t
  return (a)

def lcm(a, b):
  g = gcf(a, b)
  if (g == 0): return
  return ((a * b)//g )
  
l = int(input())
for i in range(0, l): 
    q, w = map(int, input().split())
    print(lcm(q, w))



