def f(m, n):
    return 0 if n > m else m - n


m, n = map(int, input().split())

result = f(m, n)
print(result)
