def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "Type error"
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Dividing by Zero is not allowed"
