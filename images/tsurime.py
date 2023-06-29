def calculate_points(p):
    points = p // 100  # 100円毎に1ポイント付与
    if p >= 1000:
        points += 10  # 1000円以上の買い物でボーナスポイント追加
    return points


p = int(input())

result = calculate_points(p)
print(result)
