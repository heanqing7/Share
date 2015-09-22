__author__ = 'He Anqing'
import Exception
import os
import urllib
#Share Entity
class Share:
    def __init__(self,id,type):
        self.__url = "http://table.finance.yahoo.com/table.csv?s=" + id + "." + type;
        self.__id = id;
        self.__type = type
    def getUrl(self):
        return self.__url;
    def getId(self):
        return self.__id;
    def getType(self):
        return self.__type
#download
class DownloadCsv:
    def __init__(self):
        pass;
    def download(self,share,savePath):
        if not os.path.exists(savePath):
            raise Exception.NoFileException("No Such File");
        elif not os.path.isdir(savePath):
            raise Exception.NotDirException("Not Dir");
        else:
            file = urllib.urlopen(share.getUrl());

            detailDir = savePath + share.getType()  + "\\"
            if not os.path.exists(detailDir):
                os.mkdir(detailDir)
            detailPath = detailDir + share.getId() + ".csv"
            try:
                with open(detailPath,mode="a") as f:
                    for line in file:
                        f.writelines(line)
            except Exception,e:
                raise;



