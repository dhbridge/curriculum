---
title: Moving to Phase Two
date: 2014-09-19
---

We are at the half-way point, so it is time stop briefly and think through what we have already learned. So far, we have learned to talk to your computer using the terminal. We have interacted with Python, a programming language and used Python to execute a few commands. We have also learned how to use Pip to add additional libraries to Python, and thought about using libraries like lego blocks to create new programs. 

We also learned about data and APIs. We looked at JSON as a way of structuring data and thought about what it means to represent things in this format. Then, we looked at the DPLA api and learned how to leverage libraries like DPyLA to use those APIs in our code. Finally, we saved our code in a python file that we learned how to execute in the terminal.

Well Done!

So far you have been writing code that does one thing: it get search results or prints a particular item. The power of code, however, is being able to do the same thing to a series of items and it is thinking in terms of iterating through a series that is at the core of computational thinking. To do this, we will learn two very powerful programming concepts: functions and loops.


### Asking Questions of Our Data

We have been able to do a lot with filtering the data by subject headings, by geographic space, and by contributor. But what if we want to ask questions about how the objects associated with "cooking" are described across all 10,000+ items? Say we are interested in how those descriptions of items related to cooking are gendered. How would we investigate patterns across the entirety of the DPLA's holdings related to "cooking"?

There are many ways one could go about investigating the descriptions. Work with your table to brain-storm a couple of approaches.
 

### Adding Parameters to the Query

To start, we need to restructure our query so that we can control the number of items and the "page" we get the data from. Remember that the API by default gives us 10 items at a time. We can add a parameter to our query to get up to 500 items at a time, but there were 10,909 items associated with "cooking".

Open your "my_first_script.py" file. Looking at the line that says 

	result = dpla.search('cooking')

we can change the number of items we get back by adding an additional parameter to what we pass to dpla.search. Looking at the documentation, we learn that the syntax for setting the number of items is <span class="command">page_size=</span> and the number of items we want. To get 50 items rather than 10, change that line to:

	result = dpla.search('cooking', page_size=50)

To check that this worked, let's add a line telling the computer to print out the 40th item:

	print result.items[39]

Remember, counting within a list begins at 0.

### Group Challenge

Use the [documentation](https://github.com/bibliotechy/DPyLA) and your table to add another parameter to get the information from page 3.


### Setting Up a Variable

To get all 10,000+ items associated with cooking, we need to do two things: we need to get the items all of the pages and we need a place to store them, so that as we get new items, our collections grows.

Let's tackle the second problem first. Remember back to variables? Variables are names we used to hold values. We can also use variables to hold lists. 

For example, you could create a list "fruit" that has the values "apple, orange, banana" by doing the following: fruit = ["apple", "orange", "banana"] either within a script or in the Python Interactive Shell. Now if you ask for the second item in fruit by typing "fruit[1]", you would get back "orange".

We are going to use a similar structure to save all of the items we get back from the DPLA.

Go back to "my_first_script.py". "Comment out" the line <span class="command">result = dpla.search('cooking', page_size=50)</span> by putting # at the beginning of the line. When your computer executes the file, it will skip all lines that start with a pound sign. This allows you to leave comments for yourself or to test new ways of doing things without loosing your work and tells the computer to skip this line. 

Also comment out the line you wrote to print out one of the items.

Your file should look something like this: 

	from dpla.api import DPLA

	dpla = DPLA('YourKeyHere')
	
	# result = dpla.search('cooking')
	# print result.items[1]

Now, let's create a new variable, "all_records" and set it equal to an empty list.

To do this, add a new line:

	all_records = []

This tells the computer that we have a variable, "all_records", that this variable will hold a list, and that we currently have no items in that list.

Now that we have a place to store our values, we now have to tell the computer to get the search results from each page and save those results to the "all_records" list.

### What We Learned

- To add additional parameters to our API call
- To create an empty list
- To comment-out code that we don't want to run, but want to keep
