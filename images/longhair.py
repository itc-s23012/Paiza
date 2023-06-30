def f(n):
    return "lucky" if n % 7 == 0 else "unlucky"


n = int(input().rstrip())


result = f(n)
print(result)
