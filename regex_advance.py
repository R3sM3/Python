# Desde curso de CloudAcademy
# Working with Special Characters and Anchors in Regular Expressions

import re

pattern = r'sta+r'
text = 'staar'

matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


pattern = r'sta*r'
text = 'str'

matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")



pattern = r'st.r'
text = 'staar'

matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


pattern = r'st.+r'
text = 'staar'

matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")



pattern = r'st.*r'
text = 'str'

matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")



pattern = r'sta{3}r'
text = 'str star staar staaar staaaar'

matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")



pattern = r'sta{2,3}r'
text = 'str star staar staaar staaaar'

matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")



pattern = r'.*://.*'
text = 'http://example.com'

matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")



pattern = r'(.*)://(.*)'
text = 'http://example.com'

matches = re.findall(pattern, text)
print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")
