# d = {}
# for _ in range(4):
#     x,y = map(int,input().split())
#     if x not in d:
#         d.update({x:[y]})
#         d.update({y:[x]})
#     else:
#         d[x].append(y)
#         d[y].append(x)

# print(d)

# graph = { 
#    "A" : ["b","c"],
#    "B" : ["a", "c"],
#    "C" : ["a", "b", "d"],
#    "D" : ["c"]
# }
	 
# print(graph)

import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.google.com/search?q=cute+dog&source=lnms&tbm=isch&sa=X&ved=2ahUKEwihsPaXtcX5AhW9sVYBHZSZAWcQ_AUoAXoECAEQAw&biw=1440&bih=788&dpr=2&safe=active&ssui=on"

response = requests.get(url)

print(response.text)

html = bs(response.text, "html.parser")

thumbs = html.select("a div img", limit=10)

i = 0
for thumb in thumbs:
    print(thumb["src"])
    urlretrieve(thumb["src"], str(i)+".jpg")
    i+=1