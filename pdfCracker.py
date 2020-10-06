#!/usr/bin/env python
import pikepdf
import argparse

__author__ = 'mustafauzun0'

'''
PDFCRACKER
'''

def helpMe():
	return '''
		PDFCRACKER
	'''

def main():
	parser = argparse.ArgumentParser(description=helpMe())

	parser.add_argument('-f', '--file', dest='file', help='File Path and Name', required=True)
	parser.add_argument('-d', '--dictionary', dest='dictionary', help='Dictionary Path and Name', required=True)

	args = parser.parse_args()

	pdfFilePath = args.file
	dictionaryFilePath = args.dictionary
	
	try:
		open(pdfFilePath)
	except:
		print('[-] PDF file not found please file path check')
		return

	dictionary = open(dictionaryFilePath)

	for line in dictionary.readlines():
		password = line.strip('\n')
		try:
			with pikepdf.open(pdfFilePath, password=password):
				print('[+] Password found: ' + password)
				return
		except:
			pass
		
	print('[-] Password not found.')

if __name__ == '__main__':
	main()