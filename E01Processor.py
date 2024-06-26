import AbstractExtract
import os
from base64 import *
import subprocess
import multiprocessing

class E01Processor(AbstractExtract.ExtractFrameWork):
    # _protected 
    # __private
    __dump = None
    __conf_file = "scalpel.conf"
    __mountPoint = "my_mountPoint"
    __file_pointers = list()
    def __init__(self , dump):
        # print("dump by E01 \t\t",type(dump))
        self.__dump = dump
        # self.__process_config()

    def setupDump(self):
        os.system("mkdir Playground")
        os.system("cp scalpel.conf Playground/")
        os.chdir("Playground")
        for i in self.__dump:
            name = i["name"]
            data = i["content"]
            print(f"Name: {name}, Type: {type(name)}")  # Debugging print statement
            try:
                with open(name, "wb") as f:
                    f.write(b64decode(data))
            except TypeError as e:
                print(f"Error: {e}, Name: {name}, Type: {type(name)}")  # Additional debug info

        os.mkdir(self.__mountPoint)
        self.__dump.sort(key=lambda x: x["name"])
        os.system(f"ewfmount {self.__dump[0]['name']} {self.__mountPoint}")


    def startAnalysis(self):
        print(os.getcwd())
        # os.chdir(f"Playground")
        self.run_in_separate_process(self.__extract_files, f"{self.__mountPoint}/ewf1", "Output")
        # self.cleanUp()


    def cleanUp(self):
        print("Unmounting and cleaning ....")
        os.system(f"umount {self.__mountPoint}")
        print(f"Unmounted {self.__mountPoint}")
        os.chdir(f"..")
        os.system(f"rm -r Playground")
        print(f"cleaned up ")

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

    def __extract_files(self,image_path, output_dir):
    # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

    # Define Scalpel command
        scalpel_command = [
            'scalpel', 
            '-c', 'scalpel.conf',  # Specify the path to scalpel.conf
            '-o', output_dir,      # Output directory for recovered files
            image_path             # Path to the forensic image
        ]

    # Run Scalpel command
        try:
            subprocess.run(scalpel_command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Scalpel: {e}")
        return
        
    def run_in_separate_process(self, target_function, *args):
        p = multiprocessing.Process(target=target_function, args=args)
        p.start()
        p.join()