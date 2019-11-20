def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:            
            break
    else:
        print(num)
        return True
    return False
