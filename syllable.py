import matplotlib.pyplot as pyplot
if __name__ == '__main__':
	f = open('corpus.txt', 'r')
	wr = open('output.txt', 'w')
	dictCount = dict()
	j = 0
	for line in f:
		j++
		if j < 3:
			continue
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
	plotWords = []
	plotFrequency = []
	i=0
	for k in copy:
		if i < 1000:
			plotWords.append(k[1])
			plotFrequency.append(k[0])
		wr.write('%s\t%d\n' %(k[1], k[0]))
	print plotWords
	print plotFrequency
	pyplot.plot(plotWords, plotFrequency)
	pyplot.savefig('example01.png') 
	f.close()
	wr.close()
