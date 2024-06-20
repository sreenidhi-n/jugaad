import AbstractExtract
from os import *
class E01Processor(AbstractExtract):
    __dump = None
    __mountPoint = "my_mountPoint"
    def __init__(self , dump):
        self.__dump = dump
    def setupDump(self):
        system(f"mkdir {self.__mountPoint}")
        system(f"ewfmount {self.__dump} {self.__mountPoint}")

    def startAnalysis(self):
        system(f"scalpel -c scalpel.conf -o Output_dir {self.__mountPoint}")

    def cleanUp(self):
        system(f"umount {self.__mountPoint}")
        

        
