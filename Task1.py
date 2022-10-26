# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Ответ на вопрос: Первому игроку чтобы выиграть нужно взять столько конфет, 
# сколько состовляет остаток от деления 2021 на 28, т.е 5 конфет, затем каждый раз дополнять ход соперника до 28.
from random import *
import time
def acquaintance_players():   # знакомство
    player1 = str.capitalize(input('Давайте познакомися. Как Вас зовут?\n'))
    player2 = 'Ботаня'
    return [player1, player2]


def move():
    move=['First','Second']
    if choice(move) == 'First':
        print('Слепой жребий показал - вам делать  первый ход!  ')
        first =1  
    else:
        print('Первый ход за мной! Несколько секунд, я думаю сколько мне взять конфет. Все не так просто!') 
        first=0
        time.sleep(2)
    return first    

def game(condition, firs):
    count=firs
    while condition[0] > 0:
        if not count %2:
            move= randint(1,condition[1])        # случайный выбор для хода
            if move > condition[0]:
                move= randint(1,condition[0])  
            print(f'Я забираю {move}')   
        else:
            move= int(input('Введите количество конфет, которое забираете за 1 ход '))    
            if move<1 or move>condition[1]or move> condition[0]:
                print(f'Это неправильный ход, нужно взять до 28, и не более остатка {condition[0]}')
                move= int(input('Введите количество конфет, которое забираете за 1 ход ')) 
        condition[0] = condition[0] - move
        if condition[0] > 0:
            print(f'Осталось {condition[0]} конфет')
        else:
            print('Все конфеты разобраны!')
        count += 1   
    return gamer[count%2]


print('команда start для начала работы ')
while True:
    command=input('Введите команду ')
    if command=='start':
        print('Бот-игра: "Забери конфеты!" начал свою работу')
        print('Основные правила: На столе лежит 2021 конфета. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.'
            'Все конфеты оппонента достаются сделавшему последний ход.  Заинтересовало? \n Нажмите 1 для продолжения')
    elif command== '1':
        gamer=acquaintance_players()
        print(f'Очень приятно, меня зовут {gamer[1]}')
        print('Введите команду /random для жеребьевки ') 
    elif command =='/stop':
        print('Бот остановил свою работу. Заходите еще, буду рад!')
        break  
    elif command=='help':
        print('здесь какой-то манул') 
    elif command=='/random':
        condition = [2021,28]
        firs = move()
        champion =  game(condition, firs) 
        print(f'Поздравляю! В этот раз игрок {champion}, Вы победили! Вам достаются все конфеты!')
    else:
        print('Неопознанная команда. Просьба погладить манула через /help')   
