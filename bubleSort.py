import copy
import random


def getList():
    random.randint(1,10)
    myList = []
    x = 0
    while x <= 10:
        a= random.randint(1, 10)
        myList.append(a)
        x=x+1
    originalList = copy.deepcopy(myList)
    print(originalList,"original list")
    max=len(myList)
    print(max,"length of list")
    return myList, max, originalList

def generateDefaultIndex(max:int)-> tuple:
    a = max - max
    b = a + 1
    print(a,b)
    # the current p
    return a,b

def checkValueInIndex(a,b,max):
    print(max, "max")
    # b = 12
    if b != max and b < max:
        print("pass test")

    else:
        a,b = generateDefaultIndex(max)
        print("reset a and b")

    return a,b

def iterateAB(a,b):
    a = a + 1
    b = b + 1
    return a,b

def bubbleSort(myList, a, b):
    temp = myList.pop(a)
    print(temp, "number to be bubbled")
    myList.insert(b,temp)
    print(myList,"the updated list")
    return myList




def startSort(myList, a, b):
    print(myList[a], myList[b],"numbers being compared")
    if myList[a] > myList[b]:
        print (f"{myList[a]}is higher than {myList[b]}")
        myList = bubbleSort(myList, a, b)
        return myList
    else:
        print("next loop")

def main():
   myList, max, originalList = getList()

   a,b = generateDefaultIndex(max)
   print (type(a))
   a,b = checkValueInIndex(a,b,max)
   print(a,b,"returned from test")

   x = 0
   while x < 100:
       startSort(myList,a,b)

       #--------------------------------------------------------

       a,b = iterateAB(a,b)
       print(a,b,"new nums")
       a, b = checkValueInIndex(a, b, max)
       print(a, b, "returned from test")
       x=x+1
   print (originalList,"original list")
   print(myList,"final list")

if __name__ == '__main__':
    main()