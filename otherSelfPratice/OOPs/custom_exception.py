class TimedOut(Exception):
    def __init__(self, message, timeout_value):
        msg = '{}. Timed out ofter {} seconds'.format(message, timeout_value)
        super(TimedOut, self).__init__(msg)


raise TimedOut('Failed to ping virtual machine', 600)
