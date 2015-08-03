if __name__ == '__main__':
	f = open('input.txt', 'r')
	wr = open('output.txt', 'w')
	dictCount = dict()
	for line in f:
		decodedLine = line.decode('utf-8')
		for word in decodedLine:
			if word >= u'\u0900' and word <= u'\u097F' :
				encodedWord = word.encode('utf-8')
				dictCount[encodedWord] = dictCount.get(encodedWord,0) + 1
	copy = []
	for k,v in dictCount.items():
		copy.append((v, k))
	copy = sorted(copy, reverse=True)
	for k in copy:
		wr.write('%s\t%d\n' %(k[1], k[0]))
	f.close()
	wr.close()
