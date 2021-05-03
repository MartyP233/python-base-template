# Standard Library packages
import os

# 3rd Party Libraries
import toml

# config details

globals().update(toml.load("C:\\config\\settings.toml"))