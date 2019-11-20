import logging

# 3. Write a program to check students percentage, accept percentage from user,
# if percentage is >=80 log the debug message,
# if percentage >=65 & <80 log info message,
# if percentage >=50 & <65 log warning message,
# if percentage >=35 & <50 log critical message,
# and if percenage <35 log error message.

if __name__ == "__main__":
    logging.debug("")
    logger = logging.getLogger(__name__)
    logger.level = logging.DEBUG  # setting logger to debug
    per = float(input("Enter the percentage\n"))
    #logger.level = logging.DEBUG
    print(per)
    if(per > 80):
        logger.debug("This message is debug level\n")
        logger.debug("Percentage are greater than 80\n")
    elif(per < 80 and per >= 65):
        logger.info("This message is info level\n")
        logger.info("Percentage are in between 65 and 80\n")
    elif(per < 65 and per >= 50  ):
        logger.log("This message is log level\n")
        logger.log("Percentage are in between 50 and 65\n")
    elif(per < 50 and per >= 35):
        logger.critical("This message is critical level\n")
        logger.critical("ercentage are in between 35 and 50\n")
    elif(per < 35):
        logger.error("This message is error level\n")
        logger.error("Percentage are less than 35\n")
    else:
        logger.critical("This percentage are invalid")
