# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import math
import matplotlib.pyplot as plt
import pylab
import sys
import codecs

consonants = 	[	'क','ख','ग','घ','ङ',	\
					'च','छ','ज','झ','ञ',	\
					'ट','ठ','ड','ढ','ण',		\
					'त','थ','द','ध','न',		\
					'प','फ','ब','भ','म',		\
					'य','र','ल','व',		\
					'श','ष','स','ह',		\
					'क़','ख़','ग़','ज़','ड़','ढ़','फ़','य़',	\
					'ऩ'	]
full_vowels =	[	'अ','आ',	\
					'इ','ई',		\
					'उ','ऊ',	\
					'ए',	'ऐ',		\
					'ओ','औ'	,'औ'\
					'ऑ'			]
matras =		[	'ा',		\
					'ि','ी',	\
					'ु','ू',	\
					'े','ै',	\
					'ो','ौ',	\
					'ॉ'	,'ं','़','ृ','ॄ'		]
halant = 		'्'

iIriuU =		[	'ि','ी',	\
					'ु','ू', "रि"]

yrlv =			[	'य','र','ल','व'	]

#char_type : 0 full vowel, 1 consonant, 2 consonant-matra, 3 consonant-halant
class Akshar(object):
	"""docstring for Akshar"""
	def __init__(self, name, start, char_type ):
		self.name = name
		self.start = start						
		self.char_type = char_type
		self.sound = 'U'

	def is_y_present(self):
		if self.name == "य" and self.sound == 'U':
			return True
		else:
			return False

	def is_yrlv_markedU(self):
		if self.name in yrlv and self.sound == 'U':
			return True
		else:
			return False

	def is_predecessor_iIriuU(self):
		length = len(self.name)
		if self.name[length - 1] in iIriuU or self.name == "रि":
			return True
		else:
			return False

	def is_successor_full_vowel(self):
		if self.char_type == 0:
			return True
		else:
			return False

	def change_sound(self,s):
		self.sound = s

	def return_sound(self):
		return self.sound

	def return_char_type(self):
		return self.char_type

	def return_name(self):
		return self.name

	def rule1(self):
		if self.char_type == 0 or self.char_type == 2:
			self.sound = 'F'
		elif self.char_type == 3:
			self.sound = 'H'
		elif self.char_type == 1:
			self.sound = 'U'

def printList(suchhi):
	unicode_list = repr([x.encode(sys.stdout.encoding) for x in suchhi]).decode('string-escape')
	print unicode_list

def character_type(char):
	if char in consonants:
		return 1
	elif char in full_vowels:
		return 2
	elif char in matras:
		return 3
	elif char == halant:
		return 4
	else :
		return 0

def break_syllables_word(word, syllables):
	word_list = []
	length = len(word)

	i = 0 
	while (i < length):
		char_type = character_type(word[i])
		if(char_type == 2):
			shabad = Akshar(word[i], i, 0)
		elif(char_type == 1):
			if ( i+1 < length and character_type(word[i+1]) == 3):
				shabad = Akshar(word[i]+word[i+1], i, 2)
				i = i+1
			elif ( i+1 < length and character_type(word[i+1]) == 4):
				shabad = Akshar(word[i]+word[i+1], i, 3)
				i = i+1
			else:
				shabad = Akshar(word[i], i, 1)
		else:
			return
		word_list.append(shabad)
		i = i + 1

	length_word_list = len(word_list)

	for i in range(1,9):
		if( i == 1):
			for shabad in word_list:
				shabad.rule1()
		elif( i == 2):
			j = 1;
			while j < length_word_list:
				is_y_present = word_list[j].is_y_present()
				if is_y_present:
					is_predecessor_iIriuU = word_list[j-1].is_predecessor_iIriuU()
					if is_predecessor_iIriuU:
						word_list[j].change_sound('F')
				j = j+1
		elif(i == 3):
			j = 1;
			while j < length_word_list:
				is_yrlv_markedU = word_list[j].is_yrlv_markedU()
				if is_yrlv_markedU and word_list[j-1].return_sound() == 'H':
					word_list[j].change_sound('F')
				j = j + 1
		elif(i == 4):
			j = 0 
			while j < length_word_list - 1:
				shabad_sound = word_list[j].return_sound() 
				if shabad_sound == 'U':
					is_successor_full_vowel = word_list[j+1].is_successor_full_vowel()
					if is_successor_full_vowel:
						word_list[j].change_sound('F')
				j = j + 1
		elif(i == 5):
			j = 0;
			is_seen_F = False
			while (j < length_word_list) and (not is_seen_F):
				shabad_sound = word_list[j].return_sound()
				if shabad_sound == 'U':
					word_list[j].change_sound('F')
					is_seen_F = True
				j = j + 1
		elif(i == 6):
			shabad_sound_last = word_list[length_word_list-1].return_sound()
			if shabad_sound_last == 'U':
				word_list[length_word_list-1].change_sound('H')
		elif(i == 7):
			j = 0
			while j < length_word_list-1:
				shabad_sound = word_list[j].return_sound()
				shabad_sound_successor = word_list[j+1].return_sound()
				if shabad_sound == 'U' and shabad_sound_successor == 'H':
					word_list[j].change_sound('F')
				j = j + 1
		elif(i == 8):
			j = 1
			while j < length_word_list-1:
				shabad_sound = word_list[j].return_sound()
				if shabad_sound == 'U': 
					shabad_sound_predecessor = word_list[j-1].return_sound()
					shabad_sound_successor = word_list[j+1].return_sound()
					if shabad_sound_predecessor == 'F' and (shabad_sound_successor == 'F' or shabad_sound_successor == 'U') :
						word_list[j].change_sound('H')
					else:
						word_list[j].change_sound('F')
				j = j + 1
		# for shabad in word_list:
		# 	print shabad.name + '\t' + str(shabad.sound)
		# print '\n'

	j = 0
	curr_syllable = word_list[0].return_name()
	while j < length_word_list-1:
	 	shabad_sound = word_list[j].return_sound()
	 	if shabad_sound == 'F':
		 	shabad_sound_successor = word_list[j+1].return_sound()
		 	shabad_successor_char_type = word_list[j+1].return_char_type()
		 	if shabad_sound_successor == 'F' and (not shabad_successor_char_type == 0):
		 		syllables.append(curr_syllable)
		 		curr_syllable = word_list[j+1].return_name()
		 	else:
		 		curr_syllable += word_list[j+1].return_name()
		elif shabad_sound == 'H':
			shabad_sound_successor = word_list[j+1].return_sound()
			if shabad_sound_successor == 'F':
				if j > 0:
					syllables.append(curr_syllable)
			 		curr_syllable = word_list[j+1].return_name()
				else:
					curr_syllable += word_list[j+1].return_name()
			else:
				curr_syllable += word_list[j+1].return_name()	
		else:
			curr_syllable += word_list[j+1].return_name()
		j += 1 
	syllables.append(curr_syllable)

def plot_figure(plotWords, plotFrequency, figname):
	fig = pylab.figure()
	indexes = np.arange(len(plotWords))
	width = 0.5
	plt.bar(indexes, plotFrequency, width)
	plt.xticks(indexes + width * 0.5, plotWords)
	plt.xlabel("Syllable")
	plt.ylabel("Log of syllable frequency")
	plt.show()	
	fig.savefig(figname, transparent=False, bbox_inches='tight', pad_inches=0)

if __name__ == '__main__':
	f = open('corpus.txt', 'r')
	wr = codecs.open('devnagri.txt', 'w', 'utf-8')

	devnagri_chars = consonants + full_vowels + matras + [halant]
	words = []
	for line in f:
		word = ""	
		line  = line.decode('utf-8')
		for character in line:
			if character in devnagri_chars:
				word += character
			else:
				if(len(word)):
					words.append(word)
					word = ""
		if len(word):
			words.append(word)

	syllables = []	
	for word in words:
		break_syllables_word(word, syllables)

	dictCount = dict()
	for syllable in syllables:
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
	
	plot_figure(plotWords, plotFrequency, "devnagri.jpg")

	f.close()
	wr.close()