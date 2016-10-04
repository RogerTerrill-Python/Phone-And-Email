#!/usr/bin/env python3

import pyperclip, re

phoneRegex = re.compile(r'''(       # Triple ' means multiline
    (\d{3}|\(\d{3}\))?              # Optional Area Code groups[1]
    (\s|-|\.)?                      # \s is space, - dash, or period groups[2]
    (\d{3})                         # first 3 digits groups[3]
    (\s|-|\.)                       # separator groups[4]
    (\d{4})                         # four digits groups[5]
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # any number of spaces extension groups[6] is all, group [7] is ext and groups [8] is the digits
)''',re.VERBOSE)

# Email Regex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)

# Find Matches in clipboard text.
text = str(pyperclip.paste())

matches = []            #list variable]
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])      #Grabs the phone number but standardizes to a xxx-xxx-xxxx format
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
    
# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

