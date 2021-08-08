# Standard Library packages
import os

# 3rd Party Libraries
from loguru import logger
import toml

# config details

globals().update(toml.load("C:\\config\\settings.toml"))