import logging

#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # logging.error("This is the error message.")
    # logging.warning("This is the warning message")
    # logging.critical("This is the critical message")
    # logging.info("This is the info message")
    # above info message will not printed as default log level is - 30(warning)
    #   We can get current log level as - logging.getLogger().level
    # log levels
    #   10 - debug
    #   20 - info
    #   30 - warning
    #   40 - error
    #   50 - critical
    #logging.basicConfig(level=10)
    logger = logging.getLogger(__name__)
    logger.level = logging.DEBUG # setting logger to debug
    a = 11
    if (a> 10):
        logger.info("Logging INFO Message") # this message will be printed in main logger.
        logger.debug("debug message")