# Load Libraries
import json

# Set Variables
with open("search_results.json") as json_file:
	json_data = json.load(json_file)
	
f = open('text_results.txt', 'w')

# Define Functions
def get_text(json_data):
    for each in json_data:
        # Get the Titles
        try:
            find_titles = each['sourceResource']['title']
            if isinstance(find_titles, basestring):
                title = find_titles.encode('utf8')
            else:
                for each in find_titles:
                    title = each.encode('utf8')
        except:
            title = ' '
        
        # Get the Descriptions
        try:
            find_descriptions = each['sourceResource']['description']
            if isinstance(find_descriptions, basestring):
                description = find_descriptions.encode('utf8')
            else:
                for each in find_descriptions:
                    description = each.encode('utf8')
        except:
            description = ' '

        # Get the Subject Headings
        try:
            find_subjects = each['sourceResource']['subject']
            if isinstance(find_subjects, basestring):
                subject = find_subjects.encode('utf8')
            else:
                subject_list = []
                for each in find_subjects:
                    subject_list.append(each['name'])  

                combined_subjects = ', '.join(subject_list)
                subject = combined_subjects.encode('utf8')
        except:
            subject = ' '
        
        # Combine the data into a single variable in the form of a sentence
        data = title + '; ' + description + '; ' + subject + '. \n'

		# Write the sentence to the 'text_results' file
        f.write(data)
	
# Make Function Calls
print json_data[1]
get_text(json_data)