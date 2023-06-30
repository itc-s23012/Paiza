def f(n, m, a):
    total_a = 0
    for i in range(m):
        total_a += a[i]
        if total_a > n * 60:
            return str(i)
    return "OK"


n = int(input())
m = int(input())
a = [int(input()) for _ in range(m)]

result = f(n, m, a)
print(result)
