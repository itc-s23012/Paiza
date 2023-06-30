def f(n, m):
    return "ng" if m % n else "ok"


n, m = map(int, input().split())

result = f(n, m)
print(result)
