# def hello(name):
#     print("hello" + name)

# hello("Harry")

# def hello(name):
#     return "hello" + name

# x = hello("harry")
# print(x)

# def add(a, b):
#     return a+b

# add(3, 4)

# def anything(a):
#     for i in range(0,a):
#         print(i)
# anything(10)

# def function(a):
#     if a%2 == 0:
#         print("even")
#     else:
#         print("odd")

# function(1234567)

# with open("hello.txt", "w") as f:
#     f.write("1,2,3,4,5,6,7,8,9,10")

# with open("hello.txt", "r") as f:
#     print(f.read())

# with open("hello.txt", "r") as f:
#     x = f.readline()
#     while x:
#         if(int(x)%2 == 0):
#             print(x, end='')
#         x = f.readline()

class Person:
    def hello(self):
        print("hello")

Stew_Pid = Person()
Stew_Pid.hello()
