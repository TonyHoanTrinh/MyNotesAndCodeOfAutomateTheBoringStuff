#! /usr/bin/env python3
import re

'''
Review of Regex Symbols
? matches zero or one of the preceding group
* matches zero or more of the preceding group
+ matches one or more of the preceding group
{n} matches exactly n of the preceding group
{n,} matches n or more of the preceding group
{,m} matches 0 to m of the preceding group
{n,m} matches at least n and at most m of the preceding group
{n,m}? or *? or +? performs a nongreedy match of the preceding group
^spam means the string must begin with spam
spam$ means the string must end with spam
. matches any character except newline characters
\d,\w, and \s match a digit, word or space character
\D,\W and \S match anything except a digit, word or space character
[abc] matches any character between the brackets
[^abc] matches any character that isn't between the brackets

'''
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Grouping with regex
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
print(mo.group(1))
print(mo.group(2))
areaCode, mainCode = mo.groups()
print('Area code is ' + areaCode)
print('Main code is ' + mainCode)


# Escape parenthesises
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242.')
print(mo.group())


# Matching multiple groups with pipe. Only the 1st match will be saved.
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())


# Matching strings based on common prefix
batRegex = re.compile(r'Bat(man|mobile|coptor|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))


# Optional matching
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
# Going back to the phone number example where the number may or may not have an area code
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

# Matching Zero or More with star
batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# Matching One or More with plus
batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# Matching Specific Repetitions with curly brackets
# Use {3,5} to match a range of repeats
# Greedy matching will return the longest string with {3.5}
# Non Greedy matching will return the shortest string with {3.5}? 

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

# We can use the findall() to get all occurances of the pattern
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # No groups will return a list
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # Has groups will return a tuple of lists with each list containing the groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# Creating Character Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# Negative Character Classes which matches anything not in the square brackets
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# Using ^ is also used to match patterns at the beginning
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello World!'))

# Using  $ is used to match patterns at the end
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))

# Wildcard character (matches any character except for a newline)
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# Matching Everything 
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: AL Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

# The above with dot star matches everything but a newline
# This matches everything and a newline
newLineRegex = re.compile('.*', re.DOTALL)
print(newLineRegex.search('Serve the public.\nProtect the innocent.\nUphold the law.').group())


# Case - Insensitive Matching
robocop = re.compile(r'robocop', re.I)
print(robocop.search('ROBOCOP protects the innocent.').group())

# String substitution with the sub() method
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# Grouped string substitution
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

# We can use Verbose to spread out our regex to make it for readable
phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?               # area code
        (\s|-|\.)?                       # separator
        \d{3}                            # first 3 digits
        (\s|-|\.)                        # separator
        \d{4}                            # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?     # extension
        )''', re.VERBOSE)

# We can combine arguments for the 2nd argument in re.compile
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL| re.VERBOSE)



