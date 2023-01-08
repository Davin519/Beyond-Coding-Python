# class Person:
#     def __init__(self, name, age, weight, height):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.height = height
    
#     def jump(self, dt):
#         print("jum jum jum as " + str(dt))

#     def jump_dash(self, dt):
#         self.jump(dt)
#         print("dash dash dash")
    
#     def introduce(self):
#         print("My name is " + self.name + " and " + self.age + " years old")

# Jerry = Person("Tom", 1, 50, 50)
# Tom = Person("Jerry", 2, 30, 100)
# Jerry.jump_dash(200)

# x = str(input())
# print(x.count('a'))

# x = str(input())
# for i in x:
#     print(i + " " + str(x.count(i)))

# x = input()
# y = input()
# if(y.count(x)):
#     print("True")
# else:
#     print("false")
n = 0

for i in range(1, 40):
    if(i % 2 == 0):
        n+=i
print(n)
