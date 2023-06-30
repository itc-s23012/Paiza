def f(s, n):
    return (("NG"), ("OK"))[s >= n]


s, n = map(int, input().split())

result = f(s, n)
print(result)
