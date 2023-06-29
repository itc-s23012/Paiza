def check_movie_availability(s, n):
    if s >= n:
        return "OK"
    else:
        return "NG"


s, n = map(int, input().split())

result = check_movie_availability(s, n)
print(result)
