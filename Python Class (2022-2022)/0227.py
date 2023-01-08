# d = {"a":100, "b":200}
# for i,j in d.items():  
#     print(i,j)
# ice = {"choco":100, "melona":110, "nugaba":120}
# ice.update(melona=3000)
# ice.pop("nugaba")
# for i in ice.keys():
#     print(i)
# for i in ice.values():
#     print(i)
# ice = {"choco":[2, 100], "melona":[1, 110], "nugaba":[100, 120]}
# ice["choco"][1] = 1000
# ice["nugaba"][0] = 0
# print(ice)
# a = ''
# b = a.strip()
# print(b)
# a = [1, 2, 3]
# a.append(100)
# a.insert(1, 200)
# a.pop(2)
# a.remove(1)
# a.clear()
# a.index(2)
# a.count(3)

# b = "    python     "
# b.replace("on", "off")
# c = "a b c d e"
# c.split() # ['a', 'b', 'c', 'd', 'e']
# d = ["a", "b", "c"]
# "-".join(d)
# b.upper()
# b.lower()
# b.strip()


# e = {"a":100, "b":200, "c":300}
# e.update(d=400)
# e.pop("c")
# for i, j in e.items():
#     print(i, j)
# for i in e.keys():
#     print(i)
# for i in e.values():
#     print(i)
# a = "5,000,000,000"
# a = a.replace(",", "")
# print(a)
# c = {"a":100, "b":53, "c":4389, "d":3478, "e":38}
# j = 0
# for i in c.values():
#     j=j+i
# print(j)
# ticker = "btc_krw"
# ticker = ticker.split("_")
# print(ticker)
x = input()
f = 0
for i in x:
    if i =="O":
        f=f+1
    else:
        f=f-1
print(f)

