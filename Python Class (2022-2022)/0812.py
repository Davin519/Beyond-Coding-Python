N, K = map(int, input().split())

li = list(map(int, input().split()))

count = 0
for i in range(0, len(li)-1):
    i = len(li)-1 -i
    for j in range(0 ,i):
        if li[j] > li[j+1]:
            tmp = li[j]
            li[j] = li[j+1]
            li[j+1] = tmp
            count += 1
            if count == K :
                print('{0} {1}'. format(li[j], li[j+1]))

if count < K: 
    print(-1)

