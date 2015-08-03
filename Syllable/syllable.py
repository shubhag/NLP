if __name__ == '__main__':
	f = open('input.txt', 'r')
	wr = open('output.txt', 'w')
	dictCount = dict()
	for line in f:
		decodedLine = line.decode('utf-8')
		length = len(decodedLine)
		i = 0 ;
		syllable = ""
		flag = False
		while i < length:
			if decodedLine[i] >= u'\u0900' and decodedLine[i] <= u'\u097F' and decodedLine[i]!= u'\u0964' :
				if (decodedLine[i] >= u'\u0904' and decodedLine[i] <= u'\u0939') or (decodedLine[i] >= u'\u0958' and decodedLine[i] <= u'\u0961'): 
					flag = True
					if i > 0 and decodedLine[i-1] == u'\u094D':
						syllable += decodedLine[i]
					else:
						if len(syllable):
							encodedWord = syllable.encode('utf-8')
							dictCount[encodedWord] = dictCount.get(encodedWord,0) + 1
						syllable = ""
						syllable += decodedLine[i]
				elif flag == True:
					syllable += decodedLine[i]
			else:
				flag = False
			i = i+1
		if len(syllable):
			encodedWord = syllable.encode('utf-8')
			dictCount[encodedWord] = dictCount.get(encodedWord,0) + 1	
	copy = []
	for k,v in dictCount.items():
		copy.append((v, k))
	copy = sorted(copy, reverse=True)
	for k in copy:
		wr.write('%s\t%d\n' %(k[1], k[0]))
	f.close()
	wr.close()
