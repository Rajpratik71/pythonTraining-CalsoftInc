import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def Add(a ,b):
    logger.info("in Add function")
    return a+b

def Sub(a ,b):
    logger.info("in sub function")
    return a-b

def Mul(a ,b):
    logger.info("in mul function")
    return a*b

def Div(a ,b):
    logger.info("in divide function")
    try:
        c=a/b
        return c
    except ZeroDivisionError:
        logger.error("0 as a second argument")


Add(1,2)
Mul(1,2)
Sub(1,2)
Div(1,0)

