import logging

# logs get skipped due to default log level
logging.info("Sample logging example")

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)

# If exc_info is not set to True, the output of the above
# program would not tell us anything about the exception
logging.info("End of Program")
