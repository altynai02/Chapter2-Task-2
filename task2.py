# 2) Попросить пользователя ввести слова через пробел. Отсортировать слова по количеству
# символов и вывести на экран результат.

your_text = input("Please write your text with space: ")
text = your_text.split()
text.sort(key = len) # by lenght
print(text)