# s = "hello world"

# s.replace("world", "python")
# s.split()
# "*".join(s)
# s.upper()
# s.lower()
# s.strip()

# Dictionary:

# s = {"a":100, "b":200, "c":300}
# "key":value,
# print(s["a"])(printing keys)
# s["a"] = 300(change value)
# s.update(d=10)(add and changes key and value)
# s.pop("c")(deletes items by the name.)
# s.clear(clears/delets all items)
# s.keys(takes all keys)

# for i in s.keys():
#     print(i)

# s.values(takes all values)

# for i in s.values():
#     print(i)

# s.items(takes all items(keys+values))

# for i,j in s.items():
#     print(i,j)
# s = {"a":100, "b":200, "c":300, "d":400}
# a = {}
# for i,j in s.items():
#     if j >= 300:
#         a.update({i:j})
# print(a)
# planets = {
#     "Mercury":{
#         "color":"gray",
#         "radius":"2400"
#     },
#     "Venus":{
#         "color":"rainbow",
#         "radius":"6000"
#     },
#     "Mars":{
#         "color":"red",
#         "radius":"3400"
#     }
# }
# planets["Venus"]
# if you didn't use copy(), a and b linked
# if you use copy(), only a's data copied 
# a = [1, 2, 3]
# b = a.copy()
# b[0] = 100

# c = {"test":1000}
# d = c.copy()
# d["test"] = 1
# print(c)
# d = {"a":100, "b":200}
# key = "c"
# value = 300
# d.update({"c":300})

# a = ["apple", "banana", "orange"]
# b = [400, 1300, 800]
# c = {}
# for i in range(len(a)):
#     c.update({a[i]:b[i]})
# print(c)

d = {"a":34, "b":49, "c":21}
a = 1
for i in d:
    a = a*d[i]  
print(a)
