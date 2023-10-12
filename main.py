def is_lucky_number(number):
    if len(str(number)) != 6:
        return False
    first_part = number // 1000
    second_part = number % 1000
    sum_first_part = sum(int(digit) for digit in str(first_part))
    sum_second_part = sum(int(digit) for digit in str(second_part))
    return sum_first_part == sum_second_part
result = is_lucky_number(123420)
print(result)
