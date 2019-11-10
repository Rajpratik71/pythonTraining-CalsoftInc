"""
Module to demonstrate pickle library usage in python.
"""

import pickle


GRADES = {"Alice": 89, "Bob": 72, "Charles": 87}

# Use dumps to convert the object to a serialized string
SERIAL_GRADES = pickle.dumps(GRADES)

print(SERIAL_GRADES)

# Use loads to de-serialize an object
RECEIVED_GRADES = pickle.loads(SERIAL_GRADES)
assert GRADES == RECEIVED_GRADES


SERIAL_GRADES = pickle.dumps(GRADES, protocol=pickle.HIGHEST_PROTOCOL)
print(SERIAL_GRADES)

# Use loads to de-serialize an object
RECEIVED_GRADES = pickle.loads(SERIAL_GRADES)
assert GRADES == RECEIVED_GRADES
