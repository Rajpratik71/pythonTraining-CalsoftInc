import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# logs get display as we set level to INFO
logger.info("Logging INFO Message")

# Some code

logger.info("End of program")
