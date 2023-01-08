# graph1 = {
#     "A":["B", "C", "D"],
#     "B":["A", "C"],
#     "C":["A", "B"],
#     "D":["A"]
# }
# graph2 = {
#     [0, 1, 1, 1],
#     [1, 0, 1, 0],
#     [1, 1, 0, 0],
#     [1, 0, 0, 0]
# }

# graph2 = [[0]*5 for _ in range(5)]
# for _ in range(4):
#     i, j = map(int, input().split())
#     graph2[i][j] = graph2[j][i] = 1
# print(graph2)

n = int(input())

def factorial(n):
    if n == 1:
        return n
    else:
        return n *factorial(n-1)
print(factorial(int(n)))


