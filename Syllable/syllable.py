# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import math
import matplotlib.pyplot as plt
import pylab
import sys
import codecs
if __name__ == '__main__':
	lang = sys.argv[1]
	if lang == "-hindi":
		f = open('corpus.txt', 'r')
		wr = codecs.open('devnagri.txt', 'w', 'utf-8')
		dictCount = dict()
		j = 0
		for line in f:
			j = j + 1
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
								encodedWord = syllable
								dictCount[encodedWord] = dictCount.get(encodedWord,0) + 1
							syllable = ""
							syllable += decodedLine[i]
					elif flag == True:
						syllable += decodedLine[i]
				else:
					flag = False
				i = i+1
			if len(syllable):
				encodedWord = syllable
				dictCount[encodedWord] = dictCount.get(encodedWord,0) + 1	


	elif lang == "-latinDevnagSansk":
		f = open('bgita.txt', 'r')
		wr = codecs.open('latinDevnagSansk.txt', 'w', 'utf-8')
		dictCount = dict()
		for line in f:
			decodedLine = line.decode('utf-8')
			length = len(decodedLine)
			i = 0 ;
			syllable = ""
			vowel = ['A','E','I','O','U','a','e','i','o','u', \
					'Ā','ā','Ă','ă','Ą','ą','Ē','ē','Ĕ','ĕ', \
					'Ė','ė','Ę','ę','Ě','ě','Ĩ','ĩ','Ī','ī', \
					'Ĭ','ĭ','Į','į','İ','Ō','ō','Ŏ','ŏ','Ő', \
					'ő','Ũ','ũ','Ū','ū','Ŭ','ŭ','Ů','ů','Ű','ű','Ų','ų']
			while i < length:
				if (decodedLine[i] >= u'\u0041' and decodedLine[i] <= u'\u0051') or (decodedLine[i] >= u'\u0061' and decodedLine[i] <= u'\u007A') or (decodedLine[i] >= u'\u0100' and decodedLine[i] <= u'\u017F') :
					syllable += decodedLine[i]
					if decodedLine[i] in vowel:
						i = i + 1
						while (i < length) and (decodedLine[i] in vowel):
							syllable += decodedLine[i]
							i = i +1 
						if len(syllable):
							dictCount[syllable] = dictCount.get(syllable,0) + 1	
						syllable = ""
						i = i-1
				i = i+1
			if len(syllable):
				dictCount[syllable] = dictCount.get(syllable,0) + 1	
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
			plotFrequency.append(math.log(k[0]))
		wr.write('%s\t%d\n' %(k[1], k[0]))
	f.close()
	wr.close()
	fig = pylab.figure()
	indexes = np.arange(len(plotWords))
	width = 0.5
	plt.bar(indexes, plotFrequency, width)
	plt.xticks(indexes + width * 0.5, plotWords)
	plt.xlabel("Syllable")
	plt.ylabel("Log of syllable frequency")
	plt.show()	
	fig.savefig('latinDevnagSansk.png', transparent=False, bbox_inches='tight', pad_inches=0)
