import mainpackage.controller.mathrandom as mr

if __name__=='__main__':
   print("1.random num 2.random from provided list 3.squareroot 4. cube of number 5.square of number 6.factorial")
   choice=int(input("please enter the number"))
   if choice == 1:
       print(mr.randomnum())
   elif choice == 2:
       l1=input("Provide a list seperated by ',' ")
       l1=l1.split(',')
       print(mr.randrangeany(l1))
   elif choice == 3:
       num=int(input('please enter a num for sqrt'))
       print(mr.sqrt(num))
   elif choice == 4:
       num=int(input('please enter num for cube '))
       print(mr.cubeofnum())
   elif choice == 5:
       num=int(input('please enter a num for square'))
       print(mr.squareofnum())
   elif choice == 6:
       num=int(input('enter num for finding factorial'))
       print(mr.factorial(num))
