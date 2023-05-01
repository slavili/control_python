from File import *

class WriteFile(File):
    def __init__(self, filePath, md):
        super().__init__(filePath, md)

    def setLastIndex(self, lastIndex):
        tempLink = self.getFileLink()
        tempLink.write(lastIndex)

    def updateMessage(self, userList):
        tempLink = self.getFileLink()
        mString = ''
        for k, v in userList.items():
            # v = list(v)
            v.insert(0, k)
            mString += ';'.join(v)
        tempLink.write(mString)

    def insertMessage(self, userList):
        tempLink = self.getFileLink()
        tempLink.write(';'.join(userList)+'\n')



if __name__ == '__main__':
    if os.path.isfile('db.csv'):
        rf = WriteFile('db.csv','r')
        # print(rf.insertMessage(['3','Название заметки','Содержимое заметки','2023-05-01 11:49:30.657627']))