from abc import *

class ExtractFrameWork(ABC):
    @abstractclassmethod
    def setupDump(self):
        pass
    @abstractclassmethod
    def startAnalysis():
        pass
    @abstractclassmethod
    def cleanUp():
        pass