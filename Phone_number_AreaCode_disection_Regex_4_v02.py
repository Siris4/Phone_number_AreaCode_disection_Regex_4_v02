
import re

#let's create a regex object, which we'll store in variable below:
#We create regex objects by calling "compile", and then passing it that string of
#the reg exp pattern that we are looking for xxx-xxx-xxxx.
phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d)-(\d\d\d\d)')
#\( backslash( first will literally look for a parenthesis

#we use a method of that reg exp object, called search, to search a string for this pattern.
#phoneNumRegex.search('Yo. My cell is 456-777-8888.')
#this returns a Match Object: _sre.SRE_Match object; span=(13 ,25), match='456-777-8888'
#so you want to store that in a variable, which we will call phone_number_disection
phone_number_disection = phoneNumRegex.search('Yo. My cell is (456)-777-8888.')

#the match object has a group method, which will return the entire pattern
print(phone_number_disection.group())  # or .group(0); either way, it's the same result.
print(phone_number_disection.group(1))
print(phone_number_disection.group(2))
print(phone_number_disection.group(3))
'''
(456)-777-8888
(456)
777
8888
'''








