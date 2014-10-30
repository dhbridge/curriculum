#Load Libraries
from dpla.api import DPLA
import json

#Set Variables
dpla = DPLA('19333ea341fcf105da35995eecb6356b')
# result = dpla.search('cooking', fields=['sourceResource'], page_size = 50)
all_records = []
f = open("search_results.json", "w")


# Define Functions
def pull_records(pages, end, size):
	while(pages <= end):
		paged_search = dpla.search('cooking', fields=['sourceResource'], page_size=size, page=pages)
		# print paged_search.items[2]
		save_each(paged_search)
		print "finished page " + str(pages)
		pages = pages + 1
	
def save_each(n):
	for each in n.items:
		# do something to every item in the list of items
		all_records.append(each)
		
def save_results():
	data = json.dumps(all_records)
	f.write(data)
	f.close
		
# Make Function Calls
# print result.items[39]
pull_records(1, 22, 500)
print all_records[150]
save_results()

