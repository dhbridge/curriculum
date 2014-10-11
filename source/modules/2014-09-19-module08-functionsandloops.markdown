---
title: Functions and Loops
date: 2014-09-19
---

We now have a file that looks as follows:
	
	from dpla.api import DPLA

	dpla = DPLA('Your-Key-Here')

	# result = dpla.search('cooking')
	# print result.items[1]
	
	all_records = []
	
We will now add a function that handles the query for any given page number.

### Creating a "Pull Records" Function

To write a function, we set of the function with the word "def" and then indent all of the commands that are part of the function.

In your "my_first_script.py" file, add the line

	def pull_records(pages, end, size):

You have declared a pull_records function, told the computer that this function will involve three variables (pages, end, and size) and are now ready to add the steps involving in getting the search records. These three variables are arbitrary (you could name them "snap", "crackle", and "pop") but will stand for the first page, the last page, and the number of items per page.

Tab in one space on the next line and type:

	paged_search = dpla.search(q='cooking', page_size=size, page=pages)

Your file should now look like this:

	from dpla.api import DPLA

	dpla = DPLA('Your-Key-Here')

	# result = dpla.search('cooking')
	# print result.items[1]
	
	all_records = []

	def pull_records(pages, end, size):
		paged_search = dpla.search(q='cooking', page_size=size, page=pages)

It is important to note that Python is white-space aware - when writing functions in Python, we use white space to designate what is in a function or within a loop and what is outside of it.

Let's add a print statement and test out the first stage of this function. At the same tab as "paged_search...", add:

	print paged_search.items[2]

Now to run the function, we will call the function name and give it values. On a new line and outside of the function, add the line:

	pull_records(2, 3, 50)
	
Save the file and go to terminal to run it.

### Saving Items to "All Records"

You have written and executed your first function! Well done!

Now we need to add another function to store those results to the empty "all records" array we set up in the last module. While this is not necessary when you only have one page of results, it becomes necessary when you are trying to save from multiple pages.

To set up our new "Save Each" function, we will define a new function:

	def save_each(n):

The 'n' here is again arbitrary. We are telling the function that there is one variable that we will be passing in and to take that variable and plug it in for 'n' throughout the function.

We now need to add our first loop. With how we currently have framed our request, there are 50 items in our paged_search item. We want to save each of those items separately to the "all_records" list. This means the computer needs to move through each individual item, take the item and add it to "all_records". 

Tabbing in one space on the next line under <span class="command">def save_each(n):</span>s add:

	for each in n.items:

This is called a "for loop". It tells the computer to iterate through each item in the list 'n'. We use n.items because this is the syntax from the DPyLA library. 

Now we tab in one more space and tell the computer what we want done to each item. To add the item to the "all_records" array, we use the "append" command:

	all_records.append(each)

The "save each" function should now look like this:

	def save_each(n):
		for each in n.items:
			all_records.append(each)

Now we can use this function in our "pull records" function. Currently, our "pull records" looks as follows:

	def pull_records (pages, end, size):
		paged_search = dpla.search(q='cooking', page_size=size, page=pages)
		print paged_search.items[2]

Let's delete the "print paged_search.item[2]" line, because that was just there to check that the first bit worked, and add a call to the "save_each" function, passing in our search results. Where the "print" command used to be, add:

	save_each(paged_search)

Our file should now look like:

	from dpla.api import DPLA

	dpla = DPLA('Your-Key-Here')

	# result = dpla.search('cooking')
	# print result.items[1]
	
	all_records = []

	def pull_records(pages, end, size):
		paged_search = dpla.search(q='cooking', page_size=size, page=pages)
		save_each(paged_search)

	def save_each(n):
		for each in n.items:
			all_records.append(each)

	pull_records(2, 3, 50)

To test this, let's now add a print statement to the end of the file, after the pull_records function has been run, to make sure that the items are going into the "all_records" variable.

Add:

	print all_records[30]

Save and run your script.

We have made great progress! We now have two functions to handle making the query and saving the results, but we are still only working with one "page" of search results at a time. In the next module, we will add yet another kind of loop in order to move through the different pages.

### What We Learned

- To create and call functions
- To pass variables into functions
- To create a "for loop"
- To "append" items into a list
