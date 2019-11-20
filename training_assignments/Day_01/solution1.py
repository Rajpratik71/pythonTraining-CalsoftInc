def fib(number):
    firstnumber,secondnumber=0,1
    series=''
    for i in range(number):
        series=series+str(firstnumber)+','
        firstnumber,secondnumber=secondnumber,firstnumber+secondnumber
    return(series[:-1])
def fact(number):
    if number == 1:
       return number
    else:
       return number*fact(number-1)
if __name__ == "__main__":
    operation = int(input('choose the operation to be performed 1 for fib and 2 for fact'))
    number = int(input('Give number input'))
    if operation == 1:
        print('fibonacci series is ',fib(number))
    else:
        print('factorial is',fact(number))