---
title: Writings Search Results to a File
date: 2014-09-19
published: false
---

In this module, we will focus on writing the results of our functions to a text file. This gives us a local copy of the data so that we only hit the DPLA servers once for the entire collection of files.

### Opening a new file

Our first step is to create and open a new file that we will save our search results to. In your "my_first_script.py" file, right after you declare the "all_records" variable, add:

	f = open("search_results.json", "w")

Here you are combining a function - open("search_results.json") - with the declaration of a variable. "Open" also creates a file if the file does not already exist on your computer. The "w" indicates that the file should be opened as "write". One thing to note about "w" - "write" gives the computer permission to overwrite the data inside the file, which is why we are opening the file once and writing the whole array at the end. If we were to write each item as we looped, we would end up with only the last item in the file. It would write and overwrite each item as it went along. If you need to write inside a loop, you can open the file as "a". This tells the computer to "append" the information to the end of the file, rather than overwrite the existing information. 

### Creating a "Write" Function

Now that we have a file to write to, let's create a third function to write our search results to the file. You can put this after <span class="command">f = open("search_results.json", "w")</span>.

	def save_results():
		data = json.dumps(all_records)
		f.write(data)
		f.close

First, we are creating a variable called "data". Working with json objects in python requires the use of another library, called "json", and json.dumps is an operation that helps python know how to interact with all the data in "all_records". Now, because we are using a new library, we also need to import that library at the beginning of the file. Add <span class="command">import json</span> to the top of the file. Next, we are taking our file variable from the first part of the module and writing all of the information contained in "data" to it. We then close the file.

### Calling the "Write" Function

To run the "save_results" function, we can now call the function at the end of our file.

	save_results()

Our file should now look like this:

	from dpla.api import DPLA
	import json

	dpla = DPLA('Your-Key-Here')

	# result = dpla.search('cooking')
	# print result.items[1]
		
	all_records = []
	f = open('search_results.json', 'w')

	def save_results():
		data = json.dumps(all_records)
		f.write(data)
		f.close

	def pull_records(pages, end, size):
		while(pages <= end):
			paged_search = dpla.search(q='cooking', page_size=size, page=pages)
			save_each(paged_search)
			print "finished page " + str(pages)
			pages = pages + 1

	def save_each(n):
		for each in n.items:
			all_records.append(each)

	pull_records(2, 5, 50)

	print all_records[150]

	save_results()

Test that everything is working by running your "my_first_script.py" in terminal.
You can open the "search_results.json" file to check that 200 items made it in.

### Saving all the Search Results

Now, let's change the parameters we pass to the "pull_records" function to get all of the search results.

Remember, the number we pass to "pull_records" is the first page, the second number is the last page, and the third number is the number of items per page. The DPLA will cap us at 500 items per page, so let's take '500' for our third variable. We also want to start with the first page, so '1' is our first variable.

To figure out the value we want for "end", we need to do a little math. If we have 10,909 items and can get 500 items a page, how many pages do we have to work through?

Update your "pull_records" line to:

	pull_records(1, 22, 500)

Save and run your script. This will take a bit of time, so get up, stretch, and get some coffee!

Bonus Challege: Can you write a function that determines the total number of pages from the search results?

### What We Learned

- To create and open a new file
- The difference between "write" and "append" as ways of opening a file
- To write json to a file
