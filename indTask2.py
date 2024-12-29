# Ввод предложения
sentence = input("Введите предложение: ")

# Поиск буквы "а"
position = sentence.find("а")

if position != -1:
    print(f"Буква 'а' найдена на позиции {position + 1}")
else:
    print("Буква 'а' в предложении отсутствует.")
