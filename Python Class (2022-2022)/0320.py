# def makeURL(x):
#     return "https://www." + x + ".com"
# print(makeURL("naver"))
# def strToList(a):
#     j = []
#     for i in a:
#         j.append(i)
#     return j
# print(strToList("hello"))

# def listToStr(a):
#     return(''.join(a))
# a = ['h','i']
# print(listToStr(a))
# def strToInt(a):
#     return (int(a.replace(",", "")))

# print(strToInt("1,000"))
def mct(x):
    for i in range(2, 10):
        print(i*x)
    
mct(9)