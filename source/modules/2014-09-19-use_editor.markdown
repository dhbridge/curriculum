---
title: Write Python in Script Files
date: 2014-09-19
---

In this module, we will look at how to keep save our python scripts in a text file. While the interactive shell is really useful for figuring things out, files are easier to share and enable us to keep our save our work as we go.

### Writing and Executing Script Files

First, exit out of the Python Interactive Shell by running <span class="command">exit()</span>.

You should still be in the folder we made at the beginning of the day. Check using <span class="command">pwd</span>. 

Now remember we created a file called "my_first_script.py"? Let's open that file again and remind ourselves of what we wrote.

	open my_first_script.py

It should say 'print "Hello World"'. Now that you know something about python functions, what do you expect this script to do?

Let's test it out! To execute a python file, run the following in terminal:

	python my_first_script.py

Your terminal window should look something like:

	jeriwieringa$ python my_first_script.py
	Hello World
	jeriwieringa$

Excellent! You just executed your first python script!

### Writing our DPyLA Script

Now lets recreate some of the work we did in the Interactive Shell in this script file.

Delete <span class="command">print "Hello World"</span> so that we're working with a clean file. 

First, at the beginning of a Python file we need to list the libraries that we will be using. Similar to HTML, the computer will execute the code in the order it reads it, so it is important that your commands follow a logical structure down the page. 

	from dpla.api import DPLA

Then we need to store our API key:

	dpla = DPLA('YourAPIKey')

Then we can write our search query:

	result = dpla.search('cooking') //replace with complex query

Save the file and go back to Terminal. Run 
	
	python my_first_script.py

You should notice that your computer works for awhile and then returns to normal, but doesn't tell you anything about what it did. To see results, we can use the print function again.

Open your script file again (<span class="command">open my_first_script.py</span>). 

Work with your table to add another line to the file that uses the print function to display one item from your search. 

Print is a very useful tool for checking on your script as it moves through your commands. You can use "print" to make sure your query is returning what you wanted, that your code is parsing as you expect, and to identify where things go wrong. 

### What We've Learned

- To execute python scripts in the terminal
- To write our commands in the order they should be executed
- To use print to display the results of our scripts



