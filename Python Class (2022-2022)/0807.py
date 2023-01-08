# x = input()
# y = 10

# for i in range(1, len(x)):
#     if x[i] == x[i-1]:
#         y += 5
#     else:
#         y += 10


# y = int(input())       
# for i in range(1, y+1):
#     print("*" * (y - i + 1))


x = int(input())
y = 0
for i in range(1, x+3, 2):
    print(" "*(y) + "*"*(x - i + 3))    
    y+=1

