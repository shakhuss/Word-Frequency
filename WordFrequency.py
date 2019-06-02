# Project 1
# Shakeb H.
def ReadStopWords(s):
	L = []
	with open(s, 'r', errors = 'ignore', encoding = 'utf-8-sig') as f:
		for line in f:
			line = line.replace("\n", "")
			L.append(line)
	return L



def ReadBook(s):
	with open(s, 'r', errors = 'ignore', encoding = 'utf-8-sig') as f:
		text = f.read()
		text = text.replace("\n", " ")
		text = text.replace("?", "")
		text = text.replace("!", "")				
		text = text.replace("'", "")
		text = text.replace(",", "")
		text = text.replace("“", "")
		text = text.replace("”", "")
		text = text.replace("(", "")
		text = text.replace("-", "")
		text = text.replace(")", "")
		text = text.replace("ï", "")
		text = text.replace("»", "")	
		text = text.replace("¿", "")
		text = text.replace(".", "")
	return text.lower().split(" ")

def RemoveStopWords(B,S):

	book_without_stopping = []
	for i in range(len(B)):
		word = B[i]
		if word not in S:
			book_without_stopping.append(word)
	return book_without_stopping


def getWordsandCount(Bclean):
	global count
	
	D = {}
	

	for i in range(len(Bclean)):
		word = Bclean[i]
		if word not in D:
			D.update({word:1})
		else:
			D[word] = D[word] + 1


	return D

									
def main():
	S = ReadStopWords("stopwords.txt")
	B = ReadBook("2852-0.txt")
	Bclean = RemoveStopWords(B,S)
	
	X = getWordsandCount(Bclean)
	del X['']

	count = 0
	for word in sorted(X, key=X.get, reverse=True):
		if count > 50:
			break
		count += 1

		output = "{}: {}".format(word, X[word])
		print(output)


main() 