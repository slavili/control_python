from File import *
import copy

class ReadFile(File):
    
    def __init__(self, filePath):
        super().__init__(filePath, 'r')

    def getLastIndex(self):
        tempInt = int(self.getFileLink().read())
        return tempInt

    def getMessages(self, is_list = True):
        tempList = self.getFileLink().readlines()
        self.getFileLink().seek(0)
        tempFunc = lambda m: [x.split(';') for x in m]
        tempList = tempFunc(tempList)
        tL = copy.deepcopy(tempList)
        tempDict = {row.pop(0): row for row in tempList}
        if is_list:
            return tempDict
        else:
            for i in tL:
                print('; '.join(i), end='')


if __name__ == '__main__':
    if os.path.isfile('db_test.csv'):
        rf = ReadFile('db_test.csv')
        print(rf.getLastIndex())


