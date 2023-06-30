def f(s, t):
    a = ["-"] * s
    a[t - 1] = "+"
    return "".join(a)


s = int(input())
t = int(input())

result = f(s, t)
print(result)
