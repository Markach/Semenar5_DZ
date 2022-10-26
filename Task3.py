 #Напишите программу, удаляющую из текста все слова, содержащие "абв". 

 
def search_txt(text):
    search_txt = "абв"
    lst = []
    for i in text.split():
        if search_txt not in i:
            lst.append(i)
    print(f'Результат: {" ".join(lst)}')


text= input('Введите текст через пробел: ')
print(f"Исходный текст: {text}")
search_txt(text)
