---
title: Analyzing a Subset of the Data
date: 2014-09-19
published: false
---

### Identifying Our Target Fields

Remember back to JSON and how it organizes data using key:value pairs? One of the most powerful features of JSON is that we are able to nest features and create lists within key:value pairs. This is useful for creating complex data structures. It also means that we have work within the hierarchy of key:value pairs to isolate particular values.

In order to better see that hierarchy, let's **Pretty Print** the JSON results, or print with the indentations and hierarchies visually displayed. 

Open "my_first_script.py" and **comment out** "print result.items[0]" by putting # at the beginning of the line. When your computer executes the file, it will skip all lines that start with a pound sign. This allows you to leave comments for yourself or to test new ways of doing things without loosing your work.

In order to pretty print the file, we need to load the json library. 

Under <span class="command">from dpla.api import DPLA</span>, add <span class="command">import json</span>.

Then, at the bottom of your script, add the line:

	print json.dumps(result.items[1], sort_keys=True, indent=4, separators=(',', ': '))

Save and run in Terminal. 

Work with your table to map out what this command did.

For each item in the list, we want the value of ['sourceResource']['description']. We'll put those in list called "descriptions". Then we'll use [Counter](http://pymotw.com/2/collections/counter.html) to get the most common words.

result.items[1]['sourceResource']['description']

What if we also want the titles?


What if we want to see if there is a noticible difference in the descriptions between the different contributing organizations?


// Code we need to get them to
from dpla.api import DPLA
import json
from collections import Counter
from nltk.corpus import stopwords

description_words = []
stop = stopwords.words('english')

with open("cooking_results.txt") as json_file:
	json_data = json.load(json_file)
	
print json.dumps(json_data[1], sort_keys=True, indent=4, separators=(',', ': '))

def get_words():
	for each in json_data:
		try:
			description = each['sourceResource']['description']
			words = description.split()
			for each in words:
				if each.lower() not in stop:
					if not each.isdigit():
						description_words.append(each.lower())
		
		except:
			print "no description"
			
get_words()

c = Counter(description_words)

print c.most_common(200)
