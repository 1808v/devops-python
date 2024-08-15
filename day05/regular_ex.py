#Regular Expression for Extraction Email IDs

import re

text = """"
This alert service notifies 754vivek@gmail.com and viveksharma.devops@gmail.com 

"""
#print(dir(re))

list_of_emails = re.findall("[a-z0-9\.\+-_]+@[a-z0-9\.\+-_]+\.[a-z]+" , text)

print(list_of_emails)