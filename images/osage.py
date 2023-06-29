def check_cd_capacity(n, m, durations):
    total_duration = 0
    for i in range(m):
        total_duration += durations[i]
        if total_duration > n * 60:
            return str(i)
    return "OK"


n = int(input())
m = int(input())
durations = [int(input()) for _ in range(m)]

result = check_cd_capacity(n, m, durations)
print(result)
