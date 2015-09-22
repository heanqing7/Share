__author__ = 'He Anqing'
import Config
class Factory:
    @classmethod
    def getInstance(cls):
        return Config.ConfigParser()
