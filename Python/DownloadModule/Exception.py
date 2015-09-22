__author__ = 'He Anqing'
class SavePathException(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message = message
class NoFileException(SavePathException):
    def __init__(self,message):
        SavePathException.__init__(self,message)
        self.message = message
class NotDirException(SavePathException):
    def __init__(self,message):
        SavePathException.__init__(self,message)
        self.message = message

