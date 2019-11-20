import logging
s_Handler = logging.StreamHandler()
f_Format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
s_Handler.setFormatter(f_Format)
logger = logging.getLogger(__name__)
logger.addHandler(s_Handler)
logger.setLevel(logging.INFO)
logger.info("This is info message")