# arr = list(map(int, input().split()))

# for i in range(0, len(arr)-1):
#     min_idx = i
#     for j in range (i+1, len(arr)):
#         if arr[min_idx] > arr[j]:
#             min_idx = j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i] 

# print(arr)

# arr =  list(map(int, input().split()))

# for i in range(1, len(arr)):
#     for j in range(0, i):
#         if arr[i] < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]

# arr =  list(map(int, input().split()))

# for end in range(1, len(arr)):
#     for i in range(end, 0 ,-1):
#         if arr[i-1] > arr[i]:
#             arr[i -1], arr[i] = arr[i], arr[i-1]

# print(arr)

arr =  list(map(int, input().split()))

origin = arr.copy()

answer = list()

for end in range(1, len(arr)):
    for i in range(end, 0 ,-1):
        if arr[i-1] > arr[i]:
            arr[i -1], arr[i] = arr[i], arr[i-1]

for i in range(len(origin)):
    for j in range(len(arr)):
        if origin[i] == arr[j]:
            answer.append(j)
            break



print(answer)