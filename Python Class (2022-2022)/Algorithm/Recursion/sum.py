num = int(input())
def sum(n):
    if n == 0:
        return 0
    else:
        return (n % 10 + sum(int(n / 10)))

result = sum(num)
print(result)