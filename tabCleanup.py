"""
Reformats POS-tagged files to glue words and POS tags together.
I saw a happy dog .	O V D A N P	0.945 0.869 0.998 0.932 0.893 0.983	I saw a happy dog .
=>
I\O saw\V a\D happy\A dog\N .\P
"""

from sys import argv

"""
argv[1] = tagged tweets file name
argv[2] = clean output file name
"""
if __name__ == '__main__':

	readFile = open(argv[1],"r")
	writeFile = open(argv[2],"w")

	#only include first two chunks of each line
	for line in readFile:
	    splitLine = line.split('\t')
	    words = splitLine[0].split(' ')
	    tags = splitLine[1].split(' ')
	    pairs = map(lambda x: '\\'.join(x), zip(words, tags))
	    newLine = ' '.join(pairs)
	    writeFile.write(newLine+"\n")

	print('done reformatting tagged tweets, written to ' + argv[2])
	readFile.close()
	writeFile.close()