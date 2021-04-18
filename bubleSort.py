import copy
import random

counts = 0

def getList():
	random.randint(1, 10)
	myList = []
	x = 0
	while x <= 10:
		a = random.randint(1, 10)
		myList.append(a)
		x = x + 1
	originalList = copy.deepcopy(myList)
	print(originalList, "original list")
	maxNum = len(myList)
	print(maxNum, "length of list")
	return myList, maxNum, originalList


def generateDefaultIndex(maxNum: int) -> tuple:
	a = maxNum - maxNum
	b = a + 1
	print(a, b)
	# the current p
	return a, b


def checkValueInIndex(a, b, maxNum):
	print(maxNum, "maxNum")
	# b = 12
	if b != maxNum and b < maxNum:
		print("pass test")

	else:
		a, b = generateDefaultIndex(maxNum)
		print("reset a and b")

	return a, b


def iterateAB(a, b):
	a = a + 1
	b = b + 1
	return a, b


def bubbleSort(myList, a, b):
	temp = myList.pop(a)
	print(temp, "number to be bubbled")
	myList.insert(b, temp)
	print(myList, "the updated list")
	return myList


def startSort(myList, a, b):
	print(myList[a], myList[b], "numbers being compared")
	if myList[a] > myList[b]:
		print(f"{myList[a]}is higher than {myList[b]}")
		myList = bubbleSort(myList, a, b)
		return myList
	else:
		print("next loop")


def main():
	global counts
	myList, maxNum, originalList = getList()

	a, b = generateDefaultIndex(maxNum)
	print(type(a))
	a, b = checkValueInIndex(a, b, maxNum)
	print(a, b, "returned from test")

	x = True
	while x:
		startSort(myList, a, b)

		# --------------------------------------------------------

		a, b = iterateAB(a, b)
		print(a, b, "new nums")
		a, b = checkValueInIndex(a, b, maxNum)
		print(a, b, "returned from test")

	# ---------------------------------------------------------------

		if all(myList[i] <= myList[i + 1] for i in range(len(myList) - 1)):
			x = False
		else:
			counts = counts + 1
			pass

	print(originalList, "original list")
	print(myList, "final list")
	print(f"counts = {counts}")


if __name__ == '__main__':
	main()
