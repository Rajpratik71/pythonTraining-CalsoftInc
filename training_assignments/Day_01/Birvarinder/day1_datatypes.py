def ques1():
    word=input("please enter a word whose odd index values should be removed")
    a=""
    for i in range(len(word)):
        if i%2 == 0:
            a=a+word[i]
    print(a)

def ques2():
    nums=input("enter the nums")
    a=nums.split(',')
    b=tuple(a)
    print(type(a))
    print(a)
    print(type(b))
    print(b)

def ques3():
    nums=input("enter the file name")
    a=nums.split('.')
    print(a[len(a)-1])

def ques4():
    nums=input("enter the string")
    count=0
    VOWELS=['A','E','I','O','U','a','e','i','o','u']
    for v in nums:
        if v in VOWELS:
            count = count+1
            
    print("Total vowels found in {} : {} ".format(nums,count))

def ques5():
    lis=[1,3,1,'python','java','python']
    li=set(lis)
    li=list(li)
    print(li)
    
def ques6():
    li=input("enter the values seperated by commas")
    a=li.split(',')
    b=[]
    for num in a:
        b.append(int(num))
    b.sort()
    print(b)
    print(b[len(b)-2])
        
    
def ques7():
    lis=[(10,20,40),(40,50,60),(70,80,90)]
    flis=[]
    for i in lis:
        lis1=list(i)
        lis1[2]=100
        lis1=tuple(lis1)
        flis.append(lis1)
    print(flis)

def ques8():
    mydict={1:10,2:20,3:30,4:40,5:50}
    for i in mydict:
        mydict[i]=mydict[i]+10
    print(mydict)

def ques9():
    sum=0
    d={'alex':['subj1','subj2','subj3'],'david':['subj1','subj2']}
    for i in d.values():
        sum=sum+len(i)
    print(sum)

def ques10():
    set1={"a","b","c"}
    set2={1,2,3}
    set3=set1.union(set2)
    print("union of two sets is {}".format(set3))
    set3=set1.intersection(set2)
    print("intersection of two sets is {}".format(set3))
    set3=set1.difference(set2)
    print("difference of two sets is {}".format(set3))
    set3=set1.symmetric_difference(set2)
    print("symmetric difference of two sets is {}".format(set3))
          

if __name__=='__main__':
    print("1. Write a Python program to remove the characters which have odd index values of a given string.")
    print("2. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.")
    print("3. Write a Python program to accept a filename from the user and print the extension of that.")
    print("4. Write a python program to return number of vowels in a given string.")
    print("5. Write a Python program to remove duplicates from a list")
    print("6. Write a Python program to find the second largest number in a list.")
    print("7. Write a Python program to replace last value of tuples in a list by 100.")
    print("8. Write a Python program to add the 10 to all the values of a dictionary.")
    print("9. Write a Python program to count number of items in a dictionary value that is a list.")
    print("10.Write a Python program to count number of items in a dictionary value that is a list.")
    choice=int(input("please enter your choice and press 0 to quit"))
    
    while choice != 0:
        if choice == 1:
            ques1()
            choice=int(input("please enter your choice and press 0 to quit"))
        elif choice == 2:
            ques2()
            choice=int(input("please enter your choice and press 0 to quit"))
        elif choice == 3:
            ques3()
            choice=int(input("please enter your choice and press 0 to quit"))
        elif choice == 4:
            ques4()
            choice=int(input("please enter your choice and press 0 to quit"))
        elif choice == 5:
            ques5()
            choice=int(input("please enter your choice and press 0 to quit"))
        elif choice == 6:
            ques6()
            choice=int(input("please enter your choice and press 0 to quit"))
        elif choice == 7:
            ques7()
            choice=int(input("please enter your choice and press 0 to quit"))
        elif choice == 8:
            ques8()
            choice=int(input("please enter your choice and press 0 to quit"))
        elif choice == 9:
            ques9()
            choice=int(input("please enter your choice and press 0 to quit"))
        elif choice == 10:
            ques10()
            choice=int(input("please enter your choice and press 0 to quit"))
