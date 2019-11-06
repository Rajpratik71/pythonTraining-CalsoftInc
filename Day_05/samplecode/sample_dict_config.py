import logging
from logging import config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {"standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"}},
    "handlers": {
        "default": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        }
    },
    "loggers": {
        "": {"handlers": ["default"], "level": "INFO", "propagate": False},  # root logger
        "my.packg": {"handlers": ["default"], "level": "WARNING", "propagate": False},
        "__main__": {
            "handlers": ["default"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

config.dictConfig(LOGGING_CONFIG)  # just once

main_log = logging.getLogger(__name__)  # once in each module
main_log.debug("Configured Logging.")  # message level checks at loggers first and then in handlers
main_log.error("Any Error Message.")

root_log = logging.getLogger()
root_log.warning("Warning Message.")
