import urllib.request
import itertools
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
stopwords = stopwords.words('english')


synonym_sets = []


# process user's input phrase
phrase = input("What is your phrase?")
phrase = phrase.split(" ")
phrase = [w.lower() for w in phrase]


# remember position of stopwords, but remove them
STOP = {}
for w in phrase:
	if w in stopwords:
		STOP[w] = phrase.index(w)

for w in phrase:
	if w in stopwords:
		phrase.remove(w)


# process words in the phrase
for w in phrase:

	# return a file-like object in bytes on which Python's read() method can be called
	page = urllib.request.urlopen("http://www.thesaurus.com/browse/{}?s=t".format(w))

	html_bytes = page.read()
	
	# create a BeautifulSoup object
	soup = BeautifulSoup(html_bytes, 'html.parser')

	# get senses of the word by parsing HTML
	disambiguations = []
	for x in soup.find_all("div", "synonym-description"):
		for y in x.find_all("strong"):
			try:
				disambiguations.append(y.string)
			except Exception as e:
				print(e)

	# create dictionary whose keys are senses and whose values are lists of synonyms
	# we get the list of synonyms by parsing the HTML

	DICT = {}
	i = 0
	while i < len(disambiguations):
		for x in soup.find_all("div", "relevancy-list"):
			syn_list = []
			for y in x.find_all("span", "text"):
				syn_list.append(y.string)
			syn_list.append(w)
			sense = disambiguations[i]
			DICT[sense] = syn_list
			i += 1

	# ask user to disambiguate
	print("There are {} senses of '{}'.".format(len(disambiguations), w))
	for i in disambiguations:
		print (i)

	s = input("Which sense do you want?")

	# add the list of synonyms to the synonym_sets dictionary
	synonym_sets.append(DICT[s])


# find alliterative tuples
def same_first_letter(tup):
	n = len(tup)
	i = 0
	while i in range(0, len(tup)-1):
		if tup[i][0] == tup[i+1][0]:
			i += 1
		else: break
	if i == len(tup)-1:
		return True

product = itertools.product(*synonym_sets)
for x in product:
 	if same_first_letter(x):
 		result = list(x)
 		# reinsert the stopwords
 		for s in STOP.keys():
 			result.insert(STOP[s], s)
 		print(result)





