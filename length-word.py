message_string = input('Введите строку сообщения: ')
length_message = len(message_string)
count = 0
first_symbol = 0
max_word = 0
i = 0
for i in range(length_message):
    if message_string[i] != ' ':
        count += 1
    else:
        if count > max_word:
            max_word = count
            first_symbol = i - count
        count = 0

if count > max_word:
    max_word = count
    first_symbol = i - count + 1

finish_word = message_string[first_symbol:first_symbol + max_word]

print(f'Самое длинное слово в строке: {finish_word}')

# намного более короткое решение:
# message_string = input('Введите строку сообщения: ').split()
# print(f'Самое длинное слово в строке: {max(message_string, key=len)}')
