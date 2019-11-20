import logging
#create custom logger
#create a handler
#create formatters
#add formatters to handlers
#add handlers to loggers

logger = logging.getLogger(__name__)

handler1 = logging.StreamHandler()

formatter1 = logging.Formatter('%(message)s')
formatter2 = logging.Formatter("%(asctime)s - %(message)s")

handler1.setFormatter(formatter1)

logger.addHandler(handler1)

logger.error("msg error")

handler1.setFormatter(formatter2)

logger.addHandler(handler1)
logger.error("msg error")