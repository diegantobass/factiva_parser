#/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
import csv
from collections import deque

# input should be a folder of .txt text files encoded in UTF-8
folder = sys.argv[1]

# output will be a csv file with following headers
output = csv.writer(open(os.path.join(folder, 'output.csv'), 'w'))
headers = ["count", "identifier", "title", "wordcount", "date", "publication", "code", "fulltext"]
output.writerow(headers)

# regex are used to split files into articles and find key information in them
regex_identifier = re.compile(r'(Document [a-zA-Z0-9]+)')
regex_mot = re.compile(r'.*[0-9]{1,3}\s(mots|words).*')
regex_heure = re.compile(r'[0-9]{1,2}\:[0-9]{2}')

counter = 0
for file in os.listdir(folder):
	if ".txt" in file:
		file = open(os.path.join(folder, file), 'r', encoding='UTF-8').readlines()

		accumulateur = ""
		for line in file:
			if regex_identifier.match(line):
				counter += 1
				identifier = regex_identifier.match(line)[0].split(' ')[1]

				# whenever a document ID is found, article text is split and cleaned
				text = accumulateur
				text = text.split('\n\n')
				text = [x.strip() for x in text]
				text = list(filter(lambda x: x != '', text))
				text = deque(text)
				if '\f' in text[0] or '\ufeff' in text[0]:
					text.popleft()

				# key information is extracted from the article and its header
				titre = text[0].replace('\n', ' ').strip()
				infos = deque(text[1].split('\n'))
				index_mot = ""
				for info in infos:
					if regex_mot.match(info):
						index_mot = infos.index(info)
						nb_mots = info.split(' ')[0].replace(',', '')
				if index_mot != "":
					infos = deque(list(infos)[index_mot+1:])
					date = infos.popleft()
					if regex_heure.match(infos[0]):
						infos.popleft()
					publi = infos.popleft()
					code = infos.popleft()
					article = ' '.join(list(text)[2:]).replace('\n', ' ')
				
					row = [counter, identifier, titre, nb_mots, date, publi, code, article]
					output.writerow(row)
				
				# if the header wasn't correctly parsed, give up
				else:
					print("########## Some article could not be parsed")
					# TODO : parse article that do not have title
					# TODO : parse article that have strange header formats
					# print('\n'.join(list(text)))
					print(list(text))

					print('##########\n')

				accumulateur = ""
			else:
				accumulateur += line