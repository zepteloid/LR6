# Ввод слова
word = input("Введите слово: ")

# Удаление третьей буквы
if len(word) >= 3:
    word_without_third = word[:2] + word[3:]
    print(f"Слово без третьей буквы: {word_without_third}")
else:
    print("Слово слишком короткое для удаления третьей буквы.")

# Ввод номера буквы k
k = int(input("Введите номер буквы для удаления (k): "))

# Удаление k-й буквы
if 1 <= k <= len(word):
    word_without_kth = word[:k-1] + word[k:]
    print(f"Слово без {k}-й буквы: {word_without_kth}")
else:
    print("Неверное значение k.")
