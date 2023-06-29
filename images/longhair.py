def check_lucky_number(n):
    if n % 7 == 0:
        return "lucky"
    else:
        return "unlucky"


n = int(input().rstrip())


result = check_lucky_number(n)
print(result)
