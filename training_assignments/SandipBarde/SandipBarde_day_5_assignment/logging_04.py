import logging
from logging import config

logging.config.fileConfig(fname="logConf.txt")

logging.error("This the eror message")
