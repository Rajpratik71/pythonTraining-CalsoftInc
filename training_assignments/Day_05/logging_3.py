import logging

logger = logging.getLogger(__name__)

shandler = logging.StreamHandler()
fhandler = logging.FileHandler("logs.log")
shandler.setLevel(logging.DEBUG)
fhandler.setLevel(logging.WARNING)

sformat = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
fformat = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
shandler.setFormatter(sformat)
fhandler.setFormatter(fformat)

logger.addHandler(shandler)
logger.addHandler(fhandler)

percentage = int(input("enter the percentage"))

while percentage < 100 and percentage > 0:
    if percentage >= 80:
        logger.debug("percentage >= 80")

    if percentage >= 65 and percentage < 80:
        logger.info("percentage between 80 and 65")

    if percentage >=50 and percentage < 65:
        logger.warning("percentage between 50 - 65")

    if percentage >= 35 and percentage < 50:
        logger.critical("percentage between 35 - 50")

    if percentage < 35:
        logger.error("percentage below 35")

    percentage = int(input("enter the percentage"))


