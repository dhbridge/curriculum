---
title: Looping through the Pages
date: 2014-09-19
---

In this module, we are going to learn about one of the most important programming concepts: the loop. In a loop, you tell the computer to do something to every item in a set, or in Python speak, in an list. We are going to learn about the loop while downloading all of the records associated with "cooking".

### Asking Questions of Our Data

We have been able to do a lot with filtering the data by subject headings, by geographic space, and by contributor. But what if we want to ask questions about how the materials are described across all 10,000 items associated with "cooking"? Say we are interested in how those descriptions of items related to cooking are gendered. How would we investigate patterns across the entirety of the DPLA's holdings?

There are many ways one could go about investigating the descriptions. Work with your table to brain storm a couple of approaches.


One way to investigate patterns across all of the collections is to gather all of the descriptions into a "bag of words" and see what the most common words are across all of the collections.

To start, we need to collect all of the items in the DPLA library associated with "cooking". Remember that the API by default gives us 10 items at a time. We can pass a variable to get up to 500 items at a time, but there were 10,909 items associated with "cooking". To get all of that data, we are going to use the programming concept of the **loop**. In the next module, we will be good internet citizens and save that data to a file, so that we don't repeatedly hit the DPLA's server for 10,909 items. 

### Adding Parameters to the Query

Open your "my_first_script.py" file. Looking at the line that says <span class="command">result = dpla.search('cooking')</span>, we can change the number of items we get back by adding an additional parameter to what we pass to dpla.search. Looking at the documentation, we learn that the syntax for setting the number of items is <span class="command">page_size=</span> and the number of items we want. To get 50 items rather than 10, change that line to:

	result = dpla.search('cooking', page_size=50)

To check that this worked, let's add a line telling the computer to print out the 40th item:

	print result.items[39]

Remember, counting within a list begins at 0.

Use the documentation and your table to add another parameter to get the information from page 3.


### Setting Up a Variable

To get all 10,000+ items associated with cooking, we need to do two things: we need to get the items all of the pages and we need a place to store them, so that as we get new items, our collections grows.

Let's tackle the second problem first. Remember back to variables? Variables are names we used to hold values. We can also use variables to hold lists. For example, I could create a list "fruit" that has the values "apple, orange, banana" by doing the following:

	fruit = ["apple", "orange", "banana"]

now if I ask for the second item in fruit

	fruit[1]

I will get back "orange".

We are going to use a similar structure to save all of the items we get back from the DPLA.

Go back to "my_first_script.py". Comment out the line <span class="command">result = dpla.search('cooking', page_size=50)</span> by placing a # sign at the front of the line. This tells the computer to skip this line. Also comment out the line you wrote to print out one of the items.

Your file should look something like this: 

	from dpla.api import DPLA
	import json

	dpla = DPLA('YourKeyHere')
	
	# result = dpla.search('cooking')
	# print result.items[1]

Now, let's create a new variable, "all_records" and set it equal to an empty list.

To do this, add a new line:

	all_records = []

This tells the computer that we have a variable, "all_records", that this variable will hold a list, and that we currently have no items in that list.

Now that we have a place to store our values, we now have to tell the computer to get the search results from each page and save those results to the "all_records" list.

### Getting a Range of Pages


// Code we need to get them to:

from dpla.api import DPLA

dpla = DPLA('Your-Key-Here')

all_records = []
search_term = "cooking"

		
def get_total_pages(search_term):
	result = dpla.search(search_term)
	total = result.count	
	total_pages = total/500 + 1
	return total_pages

def save_each(n):
	for each in n.items:
		all_records.append(each)

def pull_records(pages, end, size):
	while(pages <= end):
		paged_search = dpla.search(q=search_term, page_size=size, page=pages)
		print "finished page " + str(pages)
		pages = pages + 1
	
	save_results()
		
end = get_total_pages(search_term)	

pull_records(1, end, 500)	







