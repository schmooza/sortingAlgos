import copy
import random
import pandas as pd

counts = 0
dfColumnId = 1
indexIs = 1


def getList():
	random.randint(1, 10)
	myList = []
	x = 0
	while x <= 10:
		a = random.randint(1, 10)
		myList.append(a)
		x = x + 1
	originalList = copy.deepcopy(myList)
	# print(originalList, "original list")
	maxNum = len(myList)
	# print(maxNum, "length of list")
	return myList, maxNum, originalList

# def getDataFrame():
# 	df = pd.DataFrame(columns=["index"])
# 	print (df, "empty dataframe")
# 	return df

def writeCurrentListToDataFrame(myList):
	global dfColumnId

	newList = copy.deepcopy(myList)
	# print(newList, "deep copy list")

	colEnumerator = "pass" + str(dfColumnId)


	df2 = pd.DataFrame(newList,columns =[colEnumerator])
	# print(df2, "new dataframe debug")
	#
	#
	#
	#
	#
	# print(dfColumnId, "iterators")

	df2.to_csv("dataSaved/history2.csv", mode='a',index=True)
	dfColumnId = dfColumnId + 1
	return newList


def generateDefaultIndex(maxNum: int) -> tuple:
	a = maxNum - maxNum
	b = a + 1
	# print(a, b)
	# the current p
	return a, b


def checkValueInIndex(a, b, maxNum):
	# print(maxNum, "maxNum")
	# b = 12
	if b != maxNum and b < maxNum:
		pass
		# print("pass test")

	else:
		a, b = generateDefaultIndex(maxNum)
		# print("reset a and b")

	return a, b


def iterateAB(a, b):
	a = a + 1
	b = b + 1
	return a, b


def bubbleSort(myList, a, b):
	temp = myList.pop(a)
	# print(temp, "number to be bubbled")
	myList.insert(b, temp)
	# print(myList, "the updated list")
	myList = writeCurrentListToDataFrame(myList)
	return myList


def startSort(myList, a, b):
	# print(myList[a], myList[b], "numbers being compared")
	if myList[a] > myList[b]:
		# print(f"{myList[a]}is higher than {myList[b]}")
		myList = bubbleSort(myList, a, b)
		return myList
	else:
		pass
		# print("next loop")


def main():
	global counts
	myList, maxNum, originalList = getList()
	# df = getDataFrame()


	a, b = generateDefaultIndex(maxNum)
	# print(type(a))
	a, b = checkValueInIndex(a, b, maxNum)
	# print(a, b, "returned from test")

	x = True
	while x:
		startSort(myList, a, b)


		# --------------------------------------------------------

		a, b = iterateAB(a, b)
		# print(a, b, "new nums")
		a, b = checkValueInIndex(a, b, maxNum)
		# print(a, b, "returned from test")

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
