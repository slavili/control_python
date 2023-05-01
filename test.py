from ReadFile import *
from WriteFile import *
import datetime

# Начальная установка
if not os.path.isfile('db.csv'):
    createDb = WriteFile('db.csv', 'w')
    if not os.path.isfile('AI.txt'):
        createAi = WriteFile('AI.txt', 'w')
        createAi.setLastIndex('0')

while True:
    userData = input('Введите команду: ');

    if userData == 'add':
        tempList = list()
        rl = ReadFile('AI.txt')
        lI = rl.getLastIndex()
        tempList.append(f'{lI+1}')
        title = input('Введите заголовок заметки: ');
        tempList.append(title)
        content = input('Введите основной текст заметки: ')
        tempList.append(content)
        tempList.append(f'{datetime.datetime.now()}')
        # добавляем заметку
        ins = WriteFile('db.csv', 'a')
        ins.insertMessage(tempList)
        # фиксируем AUTO_INCREMENT
        createAi = WriteFile('AI.txt', 'w')
        createAi.setLastIndex(f'{lI + 1}')
        print('Заметка добавлена!')
        del createAi
        del ins
        del tempList
    elif userData == 'upd':
        mes = ReadFile('db.csv')
        userList = mes.getMessages()
        id = input('Введите идентификатор редактируемой заметки: ')
        print('Старый заголовок заметки: ', userList[id][0])
        title = input('Введите новый заголовок заметки: ');
        print('Старый основной текст заметки: ', userList[id][1])
        content = input('Введите основной текст заметки: ')
        userList[id][0] = title
        userList[id][1] = content
        userList[id][2] = f'{datetime.datetime.now()}'
        del mes
        update = WriteFile('db.csv', 'w')
        update.updateMessage(userList)
        del update
        print(f'Заметка обновлена')

    elif userData == 'del':
        print(f'Команда на {userData}')
    elif userData == 'select':
        mes = ReadFile('db.csv')
        mes.getMessages(False)
        del mes
    elif userData == 'q':
        print(f'Программа остановлена')
        break
    else:
        print(f'Команда {userData} не найдена')
