# 2) Попросить пользователя ввести слова через пробел. Отсортировать слова по количеству
# символов и вывести на экран результат.
str_text = " " # обратно в строку с пробелом
your_text = input("Please write your text with space: ")
text = your_text.split()
text.sort(key = len) # by lenght
print(str_text.join(text))