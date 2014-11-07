def biggest(aDict):
	result = None
	biggestValue = 0
	for key in aDict.keys():
		if len(aDict[key]) >= biggestValue:
			result = key
			biggestValue = len(aDict[key])
	return result

print biggest({'a': [16, 16, 9, 13, 3, 5, 8], 'b': [20, 11]})
