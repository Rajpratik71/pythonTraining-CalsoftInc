import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
f_handler = logging.FileHandler("logs.log")
f_handler.setLevel(logging.ERROR)

# Add handlers to the logger
logger.addHandler(f_handler)


class Celcius:
    def __init__(self, temp=0):
        self.set_temp(temp)

    def to_fahrenheit(self):
        return (self.get_temp() * 1.8) + 32

    def get_temp(self):
        return self.temp

    def set_temp(self, value):
        if value < -273:
            logger.error(
                f"Temprature should not go below -273, Current temprature: {value}"
            )
            # raise ValueError("Temprature should not go below -273")
            return
        self.temp = value


obj = Celcius(-277)  # ValueError
obj = Celcius(37)
print(obj.get_temp())  # 37
obj.set_temp(-300)  # ValueError
print(obj.to_fahrenheit())  # 98.600000...
