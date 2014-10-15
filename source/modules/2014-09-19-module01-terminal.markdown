---
title: Working with Your Computer
date: 2014-09-19
---

Throughout this tutorial, we will be spending a lot of time in Terminal/PowerShell as our primary way of talking to our computers. In order to do this, however, it is necessary to take some time to get comfortable working with the command line.

So let's walk through some basic commands while setting up our computer for the rest of the tutorial.

First, let's get a sense of where we are in the file structure of our computer. 

Type <span class="command">pwd</span> and press enter. 

The command, which stands for "print working directory," does exactly, tells you which directory you are in. Navigating the computer through the Terminal sometimes feels like tunneling, and 'pwd' is very helpful for seeing where you are at. You should see something like:

	/Users/yourusername

if you're on a Mac or

	C:\Users\username

for Windows.

Type <span class="command">ls</span> and press enter. 

This is another super helpful command for orienting yourself. This commands lists all the files in your current directory. If you need to see hidden files, type <span class="command">ls -a</span> (Mac) or <span class="command">ls -Hidden</span> (Windows). 

You should see something like:

	jeris-mbp:~ jeriwieringa$ ls
	Applications		Dropbox		Music
	Desktop			Envs		Pictures
	Documents		Library		Public
	Downloads		Movies		Sites		

Now that we know where we are, we now need to learn how to move around the different files. This is done with 'cd' or "change directory". If you just type 'cd', you will move back to the root of your user directory. To move forward, type 'cd [Directory_Name]'. You can also move multiple directories at a time with 'cd [Directory_Name/Directory_Name/Directory_Name]'. This way you can dig down through your files. Let's give it a try.

Type <span class="command">cd Documents</span> and press enter. Now type <span class="command">ls</span> and press enter.

You can also move backwards by typing <span class="command">cd ../</span> and to move back multiple directories, type <span class="command">cd ../../../</span>. 

Go ahead and give that a try. After moving around, work your way back to the "Documents" folder.

Let's create a folder for our work today. 

Type <span class="command">mkdir dhb_awesome</span> and press enter. Now type <span class="command">ls</span> and you should see your 'dhb_awesome' folder. Use 'cd' to move into that folder.

Folders are great but it is also helpful to know how to make files. For that, we'll use a command called 'touch' on OSX and 'New-Item' on Windows.

If you're on a Mac, type:
	
	touch my_first_script.py

and press enter. 

If you're on Windows, type:

	New-Item -ItemType file my_first_script.py

and press enter. 

Run <span class="command">ls</span> to see your file. 

To edit your new file in your default text-editor, type 
	
	open my_first_script.py

on your Mac or

	Start notepad++ my_first_script.py

on your Windows machine. This should launch your default text editor. Type <span class="command">print "Hello World"</span> into the text file and save. We will do something with that later.

If you want to know more commands, like removing files, copying files, and renaming files, checkout the [Scholars' Lab Command Line Bootcamp](http://praxis.scholarslab.org/scratchpad/bash/). But this is enough to start!


### Terminology and Mapping the Computer

Now we're going to take a step back to think about the different layers of the computer that we will be working with and about how we move data from one process to another. 

At your table, there is paper and many different drawing implements. We're going to talk through the tools and technologies we're using.  While we do that, your job is to diagram those connections using whatever metaphors or graphics that make sense to you.

The topics we will cover include:

- Working from terminal rather than interface
- Levels of Programming Languages
- Programming Libraries
- Servers
- API

### What You Have Learned

In this module, you have learned:

- to navigate and manipulate the computer using the Terminal 
- to conceptualize your computer as a computing machine connected to other computing machines

### Credits
This tutorial is based on the [Praxis Program's Command Line Bootcamp](http://praxis.scholarslab.org/scratchpad/bash/) and Greg Bloom's post, <a href="http://sunlightfoundation.com/blog/2014/06/20/opengov-voices-draw-an-api-an-interpretation-of-open-data-by-tcampers/">Draw an API</a>.