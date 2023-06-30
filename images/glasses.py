def f(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    middle_index = (len(sorted_numbers) + 1) // 2
    return str(sorted_numbers[middle_index - 1])


n = int(input())
numbers = list(map(int, input().split()))

result = f(numbers)
print(result)
