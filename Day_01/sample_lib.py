def is_prime(num):
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            break
    else:
        return True
    return False
