if __name__ == "__main__":
    zero = 0
    five = 5
    try:
        five/zero
    except ZeroDivisionError:
        print("Not allowed to devided by zero")


