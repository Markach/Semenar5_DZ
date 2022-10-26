# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. # Входные и выходные данные хранятся в отдельных текстовых файлах.

import json 
def load():
    with open('rle.json', 'r', encoding='utf-8') as rl:
        data=json.load(rl)
    print('Данные последовательности успешно загружены ')
    return data


data = load()
def rle_encode(data):
    encoding = "" 
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + data[i]
        i = i + 1
    return encoding
 

encoded_val = rle_encode(data)
print(encoded_val, '  произвели сжатие')

def save():
    with open('rle2.json', 'w', encoding='utf-8') as rl:
        rl.write(json.dumps(encoded_val,ensure_ascii=False))
    print('Наша последовательность была успешна сохранена в файле rle2.json')

save()    


def load():
    with open('rle2.json', 'r', encoding='utf-8') as rl:
        data=json.load(rl)
    print('Данные последовательности успешно загружены ')
    return data


data = load()
def rle_decode(data): 
    decode = '' 
    count = '' 
    for i in data: 
        if i.isdigit():
            count += i 
        else: 
            decode += i * int(count) 
            count = '' 
    return decode


decoded_val = rle_decode(encoded_val)
print(decoded_val, '  произвели восстановление данных')
