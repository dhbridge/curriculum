# Import Libraries
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import *
import csv

# Define Variables
with open('text_results.txt', 'r') as file:
    cooking_text = file.read().decode('utf8')

file = csv.writer(open("word_frequencies.csv", "wb"))

cooking_tokens = word_tokenize(cooking_text)
text = nltk.Text(cooking_tokens)

# Load in Stopwords Library
stopwords = stopwords.words('english')

word_set = []

# Define Functions

def normalize_text(text):
    # Work through all the words in text and filter
    for word in text:
        # Check if word is a word, and not punctuation, AND check against stop words
        if word.isalpha() and word.lower() not in stopwords:
            # If it passes the filters, save to word_set
            # If it passes the filters, save to word_set
            word_set.append(word.lower())
    return word_set
    
# Make Function Calls
#print cooking_text[0:20]
#print cooking_tokens[0:10]
#print "Concordance"
#print text.concordance('economics')
#print "Collocations"
#print text.collocations()
#print "Similar Usage"
#print text.similar('Pot')

normalize_text(text)

fd = FreqDist(word_set)
#print fd.most_common(200)
#fd.plot(50,cumulative=False)

for key, count in fd.most_common(200):
        file.writerow([key, count])