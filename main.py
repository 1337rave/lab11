def sum_in_range(start, end):
    total = 0
    for number in range(start, end + 1):
        total += number
    return total
result = sum_in_range(1, 10)
print("Сума чисел в діапазоні: ", result)
