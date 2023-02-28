def get_unique_numbers(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    unique_numbers.sort()
    return unique_numbers


numbers_sample = [10, 2, 10, 2, 3, 5, 7, 5]
unique_numbers_res = get_unique_numbers(numbers_sample)
print(f"source numbers = {numbers_sample}")
print(f"unique sorted numbers = {unique_numbers_res}")
