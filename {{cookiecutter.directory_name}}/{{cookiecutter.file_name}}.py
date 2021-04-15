# Standard Library packages
import os

# 3rd Party Libraries
import yaml

# config details

globals().update(
    yaml.safe_load(
        open(
            f"C:\\Users\\{os.getlogin()}\\some_file.yml"
        )
    )
)