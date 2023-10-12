def display_line(length, direction, symbol):
    if direction == 'горизонтальна':
        horizontal_line = symbol * length
        print(horizontal_line)
    elif direction == 'вертикальна':
        for _ in range(length):
            print(symbol)
    else:
        print("Неправильний напрямок. Виберіть 'горизонтальна' або 'вертикальна'.")
display_line(10, 'горизонтальна', '*')
display_line(5, 'вертикальна', '|')
