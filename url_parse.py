try:
	# Python 3
	from urllib.parse import urlparse, parse_qs
except ImportError:
	# Python 2
	from urlparse import urlparse, parse_qs


dictionary = {}
paramString = "siteid"


def getQParam(urlString, param):
	url = urlparse(urlString)
	query = parse_qs(url.query)
	res = "NOT_FOUND"
	try:
		res = query[param]
	except Exception as e:
		pass

	return str(res)


def addToDictionary(word):
	if word in dictionary:
		dictionary[word] = dictionary[word] + 1
	else:
		dictionary[word] = 1


def printDictionary():
	dictionary_view = [ (v,k) for k,v in dictionary.items() ]
	dictionary_view.sort(reverse=True)
	for v,k in dictionary_view:
		print(str(v) + "  " + k)


buffersize = 2**16
with open("test.txt") as f: 
	while True:
		lines_buffer = f.readlines(buffersize)
		if not lines_buffer:
			break
		for line in lines_buffer:
			addToDictionary(getQParam(line.strip(), paramString))

printDictionary()

