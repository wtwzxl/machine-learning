from numpy import *  # numpy include matrix and array data type
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir

def  createDataSet():
	# array() is functions
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels =['A','c','B','E']  # this is a list
	return group, labels
	
def classify0 (intX,dataSet,labels,k):
	# array.shape[0] return matrix rows,
	# array.shape[1] return matrix columns
	dataSetSize =dataSet.shape[0] 
	print("dataSetSize " + str(dataSetSize))
	#tile(A,(m,n)) create array[m][n] by A elements
	diffMat = tile(intX,(dataSetSize,1))-dataSet
	print(diffMat)
	sqDiffMat = diffMat**2
	print(sqDiffMat)
	# axis =1 indicates add according to rows
	#axis = 0 indicates add according to columms
	sqDistances = sqDiffMat.sum(axis = 1)
	print(sqDistances)
	distances = sqDistances**0.5 #  equal sqrt()
	# argsort() is numpy function, can get every element sorted number in matrix
	sortedDistIndicies = distances.argsort()
	print(sortedDistIndicies)
	classCount = {}
	for i in range(k):
		print(" i = "+ str(i) + "  "+str(sortedDistIndicies[i]))
		voteIlabel = labels[sortedDistIndicies[i]]
		#dict.get(key,v) if it doesn't contains key ,return 0
		classCount[voteIlabel] =classCount.get(voteIlabel,0) + 1
	# in python3  use dict.items() instead of dict.iteritems()
	#sorted(iterable, cmp=None, key=None, reverse=False)
	sortedClassCount = sorted(classCount.items(), key = operator.
	itemgetter(1), reverse = True)
	print(sortedClassCount)
	return sortedClassCount[0][0]	

def file2matrix(filename):
	love_dictionary ={'largeDoses':3,'smallDoses':2,'didntLike':1}
	fr = open(filename)
	# return file lines
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines) #get the number of lines in the file
	print("numberOfLines  " + str(numberOfLines))
	#zeros(shape,dtype = float,order = 'c')
	# create the special type array
	returnMat = zeros((numberOfLines,3))  #prepare matrix to return
	classLabelVector = []   #prepare labels return   
	index = 0
	for line in arrayOLines:
		line = line.strip() # delelte the whitespace
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		print(".......")
		print(returnMat[index,:])
		print(".......")
		if(listFromLine[-1].isdigit()):
			classLabelVector.append(int(listFromLine[-1]))
		else:
			classLabelVector.append(love_dictionary.get(listFromLine[-1]))	
		index += 1
	return returnMat,classLabelVector		

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	#shape：可以是int类型数据，或者是int类型的序列。表示新的数组的大小
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]	
	normDataSet = dataSet-tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals

def datingClassTest():
	hoRatio= 0.1
	datingDataMat,datingLabels = file2matrix('datingTestSet.txt')	
	normMat,ranges,minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs= int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:],\
		normMat[numTestVecs:m,:], datingLabels[numTestVecs:m],3)
		print("the classifier came back width :%d,the real answer is :\
		%d"%(classifierResult,datingLabels[i]))
		if(classifierResult != datingLabels[i]):
			errorCount +=1.0
	print("the total error rate is: %f " % (errorCount/\
	float(numTestVecs)))

def classifyPerson():
	resultList = ['not at all','in small doses','in large does']	
	percentTats = float(input("percentage of time spent playing video\
	games ?"))
	ffMiles = float(input("frequent flier miles earned per year ?"))
	iceCream = float(input("liters of ice cream consumed per year ?"))
	datingDataMat,datingLabels = file2matrix("datingTestSet2.txt")
	normMat,ranges, minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles,percentTats,iceCream])
	classifierResult = classify0((inArr-minVals)/ranges,normMat,\
	datingLabels,3)
	print("You will probably like this person:%s "%resultList[\
	classifierResult-1])
	
def img2vector(filename):
	returnVect = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0,32*i+j] = int(lineStr[j])
	return returnVect	
	
def handwritingClassTest():
	hwLabels = []
	# get the content dir
	trainingFileList = listdir("trainingDigits")
	m = len(trainingFileList)
	trainingMat = zeros((m,1024))
	for i in range(m):
		fileNameStr = trainingFileList[i] # load the training set
		fileStr = fileNameStr.split(".")[0] # take off .txt
		classNumStr = int(fileStr.split("_")[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:] = img2vector("trainingDigits/%s"% fileNameStr)
		testFileList = listdir('testDigits')
		errorCount = 0.0
		mTest =len(testFileList)
		for i in range(mTest):
			fileNameStr = testFileList[i]
			fileStr = fileNameStr.split(".")[0]
			classNumStr = int(fileStr.split("_")[0])
			vectorUnderTest = img2vector('testDigits/%s' %fileNameStr)
			classifierResult = classify0(vectorUnderTest,trainingMat,
			hwLabels,3)
		print("the classifier came back with: %d, the real answer is %d"\
		%(classifierResult,classNumStr))	
		if(classifierResult != classNumStr):
			errorCount += 1.0
		print('the total error rate is: %f'%(errorCount/float(mTest)))	
			
	
'''
group,labels = createDataSet()	
print(group)
print(labels)
'''
group,labels = createDataSet()	

#message =classify0([7,1],group,labels,3)
#print(message)
'''

#print(datingDataMat)
#print(datingLabels)

fig = plt.figure()
ax = fig.add_subplot(111)
# datingDataMat[:,1] indicates  the second columm of datingDataMatrix,
# datingDatmat[:,2] indicates the third column of datingDataMatrix
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],
15.0*array(datingLabels), 15.0*array(datingLabels))
#plt.show()

normMat, ranges,minVals = autoNorm(datingDataMat)
datingClassTest()
'''
datingDataMat, datingLabels = file2matrix("datingTestSet.txt")
#classifyPerson()
#handwritingClassTest()






























	
