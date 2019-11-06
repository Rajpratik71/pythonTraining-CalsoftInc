import logging

logging.basicConfig(filename="example.log", level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))

    return log_func


# @logger works like: added = logger(add) and then calling added()
@logger
def add(x, y):
    return x + y


@logger
def sub(x, y):
    return x - y


add(5, 3)
sub(5, 3)
