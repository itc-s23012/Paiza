def calculate_points(p):
    points = p // 100
    if p >= 1000:
        points += 10
    return points


p = int(input())

result = calculate_points(p)
print(result)
