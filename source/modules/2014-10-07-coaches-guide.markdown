---
title: Overview for Coaches
date: 2014-10-07
---

Welcome to being a coach for a DH Bridge workshop! This document will orient you to the goals and objectives for the day (and beyond), how the tutorials have been scaffolded, and the places where your expertise will be needed to guide participants. 

### Goals and Objectives

Coaches will need to: 

1. Be mindful of the obstacles that make it difficult for persons from underrepresented groups to learn to code, and be respectful of particpants' efforts to learn.
2. Foster collegial interaction between participants in their group, and encourage participants to collaborate and help each other when possible. 
3. Facilitate participants' forays into computational thinking by highlighting the relationships between data, content, and questions.
4. Encourage participants to avoid self-deprecating/apologetic language (I'm not sure if I'm smart enough, I'm not very good with technology, etc.). 

### Tips for the Day

1. Not all questions have solutions, errors will happen, and that's ok. Talk through participants' results, and move them toward forming their own questions to troubleshoot.
2. If a group is progressing quickly through the tutorials, have them explain back what the different lines of code are doing and/or complete the Bonus Challenges on the relevant tutorials. 
3. There shouldn't be any copying/pasting of the code.
4. Only 1 folder should be used for the entire workshop.
5. Encourage participants to add their own commments in the script files along the way.
5. Ask before taking over a participant's machine to demonstrate or fix a problem, and only do so if absolutely necessary. 
6. To make things easy on everyone, the following terminology will be used consistently throughout the day:

Terminal and Powershell = Terminal
Directories and Folders = Folders 
For Mac/Windows term translation: [http://www.dummies.com/how-to/content/comparing-common-windows-terms-with-mac-terms.html](http://www.dummies.com/how-to/content/comparing-common-windows-terms-with-mac-terms.html)

7. Capitalization is crucial in Windows Powershell, so if you see participants running into problems it's always a good idea to check there. 

### Full Day Schedule

Note: the timeblocks are suggestions and will depend on the progress of your group. The first half of the day is primarily concerned with introducing thinking computationally: how a computer processes information locally and with other computers. The second half of the day builds on this foundation to address computational thinking about humanities data: how to utilize computation to ask questions and work with the kinds of data that interest humanities scholars.

**9:30-10:20a** Welcome and Setting Up the Learning Environment: goals and objectives for the day, introductions within small groups. Coaches' Project Demonstrations: current projects and problems

10 Minute Break

**10:30-Noon:** Modules 1-5

LUNCH

**1:00-2:30p:** Modules 6 - 8

10 Minute Break

**2:40-4:00p:** Modules 9 - 11

**4:00-5:00p:** Modules 12 - 13

**5:00-5:30:** Wrapup (recap the day and tips for continued learning)

**5:30:** Decompressing and socializing

### Tutorial Modules

- [Installation](#installation)
- [Module 1](#one)
- [Module 2](#two)
- [Module 3](#three)
- [Module 4](#four)
- [Module 5](#five)
- [Module 6](#six)
- [Module 7](#seven)
- [Module 8](#eight)
- [Module 9](#nine)
- [Module 10](#ten)
- [Module 11](#eleven)
- [Module 12](#twelve)
- [Module 13](#thirteen)

### Installation

Check to make sure that participants have the following installed and ready to go:

1. Python 2.7
2. `pip`
3. Text Editor: work with participants to set TextWrangler as the default text editor for Mac users. It's not an issue for Windows users because the commands specify starting Notepad++ each time. 
4. Chrome browser

If possible, please have participants pin the text editor and Chrome to their Dock (Mac)/Taskbar (Windows), or at least have them easily accessible. 

### One

(To be done with the full group)

**Learning Checks:**

1. After your group members have all created their "dhb_awesome" folder have them find where it lives on their computer through Finder/My Computer. Also have them find their newly created "my_first_script.py" file. Have them compare the directory path with what they did in Terminal to ensure they can see that they are creating files and folders on their local machine.   

### Two

**Module Goal:** to understand how computers talk to one another (through the syntax of API requests) and how computers display data (as a data dump vs. JSON).

Beginning Activity: 
Start with the DPLA interface in the browser and have your group search for "cooking". Have your group read what's going on in the URL. Filter the number of items displayed using the GUI's filters. How did the URL change? What's the syntax?  

**Learning Checks:**
 
1. Have them talk through the API request URL to reinforce understanding of the structure of the request.
2. Review how JSON stores data items as objects and how it displays those objects.


### Three

**Module Goal:** to understand the benefits of installing libraries via `pip`, and the relationship between the Python Interactive Shell and Terminal in the local machine.

**Learning Checks:** 

1. Make sure participants are clear on difference between Python Interactive Shell and Terminal.
2. Terminology check: string, variable, array/list

### Four

**Module Goal:** to understand how to create targeted queries for data and generally the different kinds of questions that can be pursued/answered based on those queries.

**Learning Checks:**

1. Constructing additional queries: highlight the questions that would motivate the choice of different commands and filtering of results.
2. See if there are any general questions about APIs and the documentation used in the module. 

### Five

**Module Goal:** to understand how programming languages interact with computers and the basic function and purpose of libraries.

**Learning Checks:**

1. **Mapping Exercise #1:** have participants diagram the following, similar to the API exercise from earlier in the day:
-High-level programming languages (like Python) enable you to write commands for your computer in something that approximates English. Those commands are then translated down to machine language, executed by the hardware, and the results are translated back to generate the desired output. Your computer is constantly processing commands from the applications on your machine in multiple programming languages. Just like those applications, you can use the terminal interface to send commands to your computer.
-Discuss everyone's diagrams and make sure the concepts are clear.

3. **Mapping Exercise #2:** have participants diagram the following, similar to the API exercise from earlier in the day:
-A Python module or library is a bundle of code, including variables and functions (defined processes), that does a particular task. Many Python modules already exist out in the world, ready to be used, and new ones are developed by programmers all the time. Python scripts, which combine these modules with additional python commands, give the computer new, and more complicated, tasks that can be completed.
-Discuss everyone's diagrams and make sure the concepts are clear.

### Six

**Module Goal:** how to begin focusing on the data relevant to the research questions at hand and selecting the relevant aspects to further pursue those questions.

Before your group jumps into the code-heavy part of the module, start off with the quick review of how script files should be organized. There will also be a handout for participants to reference as they continue through the modules. Participants may be tempted to gloss over this part, but make sure they take the time to get the format down. 
1. load libraries
2. set variables to be used throughout the script
3. define all functions
4. make calls/commands to execute the functions

Optional Activity: have participants create their own mnemonic device for the above format (LSDM)

Terminology related to functions: from now on the tutorials will heavily use new phrases to describe how the functions work in relation to the data. These phrases are part of programming vernacular, and so they're not jarring to participants, here are some basic definitions to maintain consistency:
1. call: to execute 
2. declare/set: create a new function
3. pass: to run data through the function/loop

**Learning Checks:**
1. Have a quick discussion about the merits of commenting out versus deleting lines
2. Verify that participants understand setting variables and how they can hold lists (an empty list so far).

### Seven

**Learning Checks:** 
1. Review and explain in a group discussion: how functions can be combined to solve problems, with the example of the two functions written so far and how they work together.
2. Review what "append" does.
3. Group challenge: talk through the functionality and uses for a "for loop"

### Eight

**Learning Checks:** 
1. Group challenge: along with talking through how a "while loop" works, also review why the "while loop" is added into the function where it is. 

### Nine
Questions for the participants to discuss/keep in mind throughout the module:
1. 

**Learning Checks:**
1. The value of working locally: writing the search results to a JSON file gives the flexibility for working with a large collection of files on a local machine without having to constantly hit the DPLA (or any other API servers) and to find patterns that we could not find using the online interface for the DPLA's holdings.
2. When to use "append": writing inside a loop, which allows the comupter to add the information it grabs to the end of the file rather than overwriting what's there each time. 

### Ten
Questions for the participants to discuss/keep in mind throughout the module: 
1. Are there other data fields to include that would help address the research question? 
2. What other research questions can you ask of this data?

**Learning Checks:**
1. Dealing with the realities of messy data: pristine datasets are extremely rare. In our example, the "cooking" data features many items that don't have information for the three fields that we're focusing on. 
2. Open your "text_results.txt" file in TextWrangler/Notepad++ and scroll through what was saved. What do you notice? What information is/isn't there? What kinds of hypotheses can you make based on these results?

**We anticipate this will be as far as participants can get in one day without getting too frustrated or burned out. If that's the case, encourage them to talk through what they've already done, clarify parts that are still mysterious/confusing, and/or go back to the earlier modules and work through with different search terms and parameters. They can also do the activity posed as a Learning Check in Module 13.

### Eleven
Questions for the participants to discuss/keep in mind throughout the module:
1. How is the script parsing the text data? 
2. What are the benefits and limitations of breaking the data into chunks in this way?
3. How would you speak to the ways you as the researcher have shaped this dataset to a colleague?

**Learning Checks:** 
1. Words and tokens: what is NLTK considering a "word"? what is a token? 
2. Collocations, concordances, and "similar": what are they doing? what analytical value does each have for the research question at hand and for your own work? 

### Twelve
Questions for the participants to discuss/keep in mind throughout the module: 
1. How does the results generated by the text mining script compare to your own hypotheses? 
2. What kinds of research projects and questions benefit from this approach? 

**Learning Checks:**
1. Stopwords: what makes up these lists? how does one need to account for different stopwords based on the research at hand, language, corpus, etc.?
2. Encourage participants to checkout the documentation for [NLTK](http://www.nltk.org/) to get a better sense of what else it can do.  

### Thirteen
Questions for the participants to discuss/keep in mind throughout the module:
1. What are the benefits of having the data in a CSV file?
2. What else can you do with the data that's now in the CSV file? 

**Learning Checks:**
1. Have participants pull out their diagrams of Terminal, API, and programming languages and make any necessary revisions based on what they've learned throughout the day. 











