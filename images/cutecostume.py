def check_candy_pack(n, m):
    if m % n == 0:
        return "ok"
    else:
        return "ng"


# 入力を受け取る
n, m = map(int, input().split())

# 結果を出力
result = check_candy_pack(n, m)
print(result)
