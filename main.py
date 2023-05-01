from ReadFile import *
from WriteFile import *
import datetime

# Начальная установка
if not os.path.isfile('db.csv'):
    createDb = WriteFile('db.csv', 'w')
    if not os.path.isfile('AI.txt'):
        createAi = WriteFile('AI.txt', 'w')
        createAi.setLastIndex('0')

rl = ReadFile('AI.txt')
# print(rl.getLastIndex())
dt_now = datetime.datetime.now()

mes = ReadFile('db.csv')
# mes.getMessages(False)
# print(mes.getMessages())
userList = mes.getMessages()
print()
# print(mes.getMessages())
print(userList)
userList['1'][0] = 'Заметка про мальчика'
userList['1'][1] = 'Заметка про нашего мальчика дядю Фёдора!!!!'

update = WriteFile('db.csv','w')
update.updateMessage(userList)
update = ''

lI = rl.getLastIndex()
ins = WriteFile('db.csv','a')
ins.insertMessage([f'{lI+1}','Название заметки3','Содержимое заметки3',f'{dt_now}'])
ins = ''

createAi = WriteFile('AI.txt', 'w')
createAi.setLastIndex(f'{lI+1}')
createAi = ''

# mes = ReadFile('db.csv')
mes.getMessages(False)
print()



