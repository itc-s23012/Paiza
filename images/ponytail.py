def check_vision_test_results(results):
    correct_count = sum(
        [1 for result in results if result.split()[0] == result.split()[1]]
    )
    return "OK" if correct_count >= 3 else "NG"


results = [input() for _ in range(5)]

result = check_vision_test_results(results)
print(result)
