__author__ = 'He Anqing'
class ConfigParser:
    def __init__(self,path=None):
        self.__path = path;
        self.__lines = list();
        self.__map = dict();

    def setPath(self,path):
        self.__path = path

    def parse(self):
        self.__readfile();
        for line in self.__lines:
            t = line.split("=")
            self.__map[t[0]] = t[1];
        return self.__map;

    def __readfile(self):
        with open(self.__path) as f:
            for line in f:
                if line[0] == "#":
                    continue;
                else:
                    # notice : delete the last '\n'   notice [x:y]
                    if line[-1] == '\n':
                        lineNoEndl = line[0:-1]
                    else:
                        lineNoEndl = line
                    self.__lines.append(lineNoEndl)

