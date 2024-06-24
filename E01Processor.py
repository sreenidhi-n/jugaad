import  AbstractExtract
from os import *

class E01Processor(AbstractExtract.ExtractFrameWork):
    # _protected 
    # __private
    __dump = None
    __conf_file = "scalpel.conf"
    __mountPoint = "my_mountPoint"
    __file_pointers = list()
    def __init__(self , dump):
        self.__dump = dump
        # self.__process_config()

    def setupDump(self):
        system(f"mkdir Playground")
        system(f"cp scalpel.conf Playground/")
        chdir(f"Playground")
        system(f"mkdir {self.__mountPoint}")
        system(f"ewfmount {self.__dump} {self.__mountPoint}")
        
        


    def startAnalysis(self):
        chdir(f"cd Playground")
        system(f"scalpel -c scalpel.conf -o Output_dir {self.__mountPoint}")

    def cleanUp(self):
        chdir(f"cd Playground")
        system(f"umount {self.__mountPoint}")
        chdir(f"..")
        system(f"rm -rf Playground")

    def __process_config(self):
        # Create a dictionary to store config content by format
        config_sections = {}
        current_section = None

        # Read the input config file
        with open(self.__conf_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith("#"):
                    # New section header
                    current_section = line[2:].strip().replace("/", "_")
                    config_sections[current_section] = []
                elif current_section:
                    # Add line to the current section
                    config_sections[current_section].append(line)

        # Write each section to a separate config file
        for section, lines in config_sections.items():
            output_file = f'scalpel_{section}.conf'
            with open(output_file, 'w') as f:
                for line in lines:
                    f.write(line + '\n')
            self.__file_pointers.append(output_file)


        
