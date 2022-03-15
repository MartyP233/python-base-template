# Standard Library packages
import os

# 3rd Party Libraries
from dotenv import load_dotenv
from loguru import logger

# Internal modules

######################### Config Details ############################

logger.add("logs/{{ cookiecutter.file_name }}.log", rotation="12:00")

load_dotenv()


######################### Functions #################################



#####################################################################

def main():
    pass

if __name__ == "__main__":
    main()