---
title: Working with Local Data
date: 2014-09-19
---

Now that we have a very large file of JSON data, we can work locally to find  patterns that we could not find using the online interface for the DPLA's holdings. 

In this module, we will create a new script and learn how to load data from our "search_results.json" file. We will also install the Natural Language ToolKit library in order to do some text analysis on our data.

### Loading from a Local File

It is time to create a new script file!

Go to terminal and type:

	touch my_second_script.py

To open your new script file, type:

	open my_second_script.py

To begin, let's load in some of the libraries we will need for this next phase of the workshop.

First, we will need the json library again. To add this, type <span class="command">import json</span> at the very top of the file.

We are also going to use a library called "collections" and a specific part of that library called "Counter". To import this, type <span class="command">from collections import Counter</span> on the next line.

The next thing is to load up the data from our "search_results.json" file.

The structure for this is:

	with open("search_results.json") as json_file:
		json_data = json.load(json_file)

Here, we tell Python to "open" our "search_results.json" file and assign it to the variable "json_file". The we use the "load" method in the "json.library" to load up the data and save it as the variable "json_data". 

To make sure this worked, let's print out one item from the json data. Work with your table to add a print statement to print the second item in the json_data list.


### Installing NLTK

We are interested in the languaged used in the "description" fields across all the "cooking" items in the DPLA database. Fortunately, there is good support within Python for text analysis and one power library we can use is the Natural Language ToolKit (or NLTK).

To install NLTK, let's go back to our terminal and use pip.

Run <span class = "command">pip install nltk</span>. You may need to use <span class="command">sudo pip install nltk</span>.

Now, go back to your file and import nltk at the top of the file.

There are also a number of datasets available for use with nltk. For our purposes, we will only be using the 'stopwords' dataset, but browse the list of all the datasets you could download and use at [http://www.nltk.org/nltk_data/](http://www.nltk.org/nltk_data/). 

To download the stopwords, we are going to go back into the Python Interactive Shell. Run <span class="command">python</span>. Your terminal window should now look something like this:

	Python 2.7.5 (default, Mar  9 2014, 22:15:05)
	[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 

Type <span class="command">import nltk</span> and press enter.

Next type <span class="command">nltk.download('stopwords')</span> and press enter.

Great!

Now we need to load these stopwords into our Python file. Switching back to our "my_second_script.py" file, add <span class="command">from nltk.corpus import stopwords</span> to the top of the file.

We are now ready to start working with our data.

### What We Learned

In this module, we have reviewed and learned:

- to create new files using terminal
- to load json data from a file 
- to download libraries using pip
- to download datasets within libraries
- to load libraries into our scripts

