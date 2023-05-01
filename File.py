import os

class File():
    def __init__(self, filePath, md):
        self.__fileLink = open(filePath, md, encoding='UTF-8')


    def getFileLink(self):
        return self.__fileLink

    def __del__(self):
        self.__fileLink.close()

if __name__ == '__main__':
    if os.path.isfile('db_test.csv'):
        rf = File('db_test.csv','r')
    else:
        rf = File('db_test.csv', 'w')
