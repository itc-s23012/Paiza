def display_progress(s, t):
    progress = ["-"] * s
    progress[t - 1] = "+"
    return "".join(progress)


s = int(input())
t = int(input())

result = display_progress(s, t)
print(result)
