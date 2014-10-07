---
title: Writings to a File
date: 2014-09-19
published: false
---

In this module, we will focus on writing the results of our loops to a new text file. This gives us a local copy of the data so we don't have to hit the DPLA's servers repeatedly as we work out our code.

### 

// Code to add to save to file
f = open("cooking_results.txt", "w")

def save_results():
	data = json.dumps(all_records)
	f.write(data)
	f.close
	
save_each(paged_search)