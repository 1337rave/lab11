def display_odd_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number)
display_odd_numbers(1, 10)
