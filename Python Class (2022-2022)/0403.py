# f = open("hello.txt", "w")
# for i in range(1, 11):
#     f.write(i)
# f.close()
# a = [1,2,3,4]
# a[0] = 100
# j = 0
# for i in range(1, 10, 1):
#     j+=i
# print(j)
# for i in range(1, 254798):
#     if(20%i == 0):
#         print(i)
# x = int(input())
# c = 0
# for i in range(1,x+1):
#     if(x%i == 0):
#         c+=1
# if c == 2:
#     print("prime")
# else:
#     print("not prime")
x = {"a":100, "b":200, "c":300}
y = 0
for i in x.values():
    y+=i
print(x)