__author__ = 'He Anqing'
import ConfigModule.ConfigFactory as CF;
#sigleton
def singleton(cls,*args):
    instance = {}
    def _singleton(*args):
        if cls not in instance:
            instance[cls] = cls(*args)
        return instance[cls]
    return _singleton

@singleton
class SystemInfo:
    def __init__(self,path):
        self.__path = path
        self.__fill()
    def __load(self):
        configParser = CF.Factory.getInstance();
        configParser.setPath(self.__path);
        return configParser.parse()
    def __fill(self):
        d = self.__load()
        self.__LOGLEVEL = d["LOGLEVEL"]
        self.__CSVSAVEPATH = d["CSVSAVEPATH"]

    def getLogLevel(self):
        return self.__LOGLEVEL;
    def getCsvSavePath(self):
        return self.__CSVSAVEPATH;
