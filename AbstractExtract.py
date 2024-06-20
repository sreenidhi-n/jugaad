from abc import *

class ExtractFrameWork(ABC):
    @abstractclassmethod
    def setupDump(self,dump):
        pass
    @abstractclassmethod
    def startAnalysis():
        pass
    @abstractclassmethod
    def cleanUp():
        pass