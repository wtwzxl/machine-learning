from math import log

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = { }
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	print(labelCounts)
	for key in labelCounts:
#the the number of unique elements and their occurance		
		prob = float(labelCounts[key])/numEntries  
		shannonEnt -= prob*log(prob,2)  #log base 2
	return shannonEnt		

def createDataSet():
	dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	labels = ['no surfacing','flippers']
	return dataSet, labels
	
def splitDataSet(dataSet,axis,value):
	retDataSet = [ ]	
	for featVec in dataSet:
		if(featVec[axis] == value):
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis +1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0])-1 # the last element is classify label so need substract 1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain =0.0
	bestFeature = -1
	for i in range(numbFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet,i,value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob*calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if( infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature

myData,labels = createDataSet()
print(myData)
print(labels)
result = calcShannonEnt(myData)
print(result)	
'''
myData[0][-1] = 'maybe'	
result = calcShannonEnt(myData)	
print(result)	
'''
reDataSet= splitDataSet(myData,0,1)
print(reDataSet)






























