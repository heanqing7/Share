__author__ = 'He Anqing'
class Log:
    def __init__(self,path=None):
        self.__path = path;
    def setPath(self,path):
        self.__path = path;
    def log(self,level,message):
        pass;
