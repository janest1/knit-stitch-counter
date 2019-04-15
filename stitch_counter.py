#read in each line, perform the calculation, save row and stitch count in dict

import re
import sys
import textract

produce = {'M': 1,
			'K2tog': -1,
			'K3tog': -2,
			'Ssk': -1}

consume = {}


def get_rows(text):
	
	cast_on_match = re.search('(cast on )(\\d+)(\\s)', text, flags=re.I)
	begin = cast_on_match.start()
	pattern = text[begin:].replace('\n', ' ')

	row_count = {}
	# row 0 = number of cast on stitches
	row_count[0] = cast_on_match.group(2)
	rows = re.split('\\d+[a-z]{2} row:|Next row:', pattern)[1:]

	for i, row in enumerate(rows):
		repetition = re.search('\\*.*?\\*', row)
		consumed = row_count[i]
		if repetition:
			remain_match = re.search('(to last )(\\d+)( sts)', row)
			if remain_match:
				remaining = remain_match.group(2)
			else:
				remaining = consumed
	

if __name__ == '__main__':
	# text = textract.process(sys.argv[1]).decode('utf-8')
	text = textract.process('ribbedtanktoppattern.pdf').decode('utf-8')
	# get_rows(sys.argv[1])
	get_rows(text)
