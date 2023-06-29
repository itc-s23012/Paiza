def check_candy_pack(n, m):
    if m % n == 0:
        return "ok"
    else:
        return "ng"


n, m = map(int, input().split())

result = check_candy_pack(n, m)
print(result)
