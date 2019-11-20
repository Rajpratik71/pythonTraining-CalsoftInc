class ComplexNumbers:
    def __init__(self, real,sign,img):
        self.real = real
        self.sign = sign
        self.img = img
    def Display(self):
        print("{}{}{}j".format(self.real,self.sign,self.img))

    def __add__(self, other):
        self.real += other.real
        self.img  += other.img
        if self.img > other.img:
            self.sign = self.sign
        else:
            self.sign = ComplexNumbers.sign
        return  self

if __name__ == "__main__":
    firstNumber  = input("Enter the first complex number\n")
    first_sign = ""
    first_real = 0
    first_img  = 0
    firstNumber = firstNumber.replace(" ", "")
    firstList = firstNumber.split('+')


    if len(firstList) == 2:
        first_sign = "+"
        first_real = int(firstList[0])
        firstImg = firstList[1]
        first_img = int(firstImg[0:len(firstImg) - 1])
    else:
        firstList = firstNumber.split('-')
        if len(firstList) == 2:
            first_sign = "-"
            first_real = int(firstList[0])
            firstImg = firstList[1]
            first_img = int(firstImg[0:len(firstImg) - 1])
        else:
            first_sign = "-"
            first_real = int(firstList[1])
            first_real = 0 - first_real
            firstImg = firstList[2]
            first_img = int(firstImg[0:len(firstImg) - 1])

    obj1 = ComplexNumbers(first_real, first_sign, first_img)
    obj1.Display()

    secondNumber  = input("Enter the second complex number\n")
    second_sign = ""
    second_real = 0
    second_img  = 0
    secondNumber = secondNumber.replace(" ", "")
    secondList = secondNumber.split('+')
    if len(secondList) == 2:
        sign = "+"
        second_real = int(secondList[0])
        secondImg = secondList[1]
        second_img = int(secondImg[0:len(secondImg) - 1])
    else:
        secondList = secondNumber.split('-')
        if len(secondList)==2 :
            sign = "-"
            second_real = int(secondList[0])
            secondImg = secondList[1]
            second_img = int(secondImg[0:len(secondImg) - 1])
        else:
            sign = "-"
            second_real = int(secondList[1])
            second_real = 0 - second_real
            secondImg = secondList[2]
            second_img = int(secondImg[0:len(secondImg) - 1])
    obj2 = ComplexNumbers(second_real, sign, second_img)
    obj2.Display()

    obj3 = obj1 + obj2
    obj3.Display()

