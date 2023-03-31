# Desde curso de CloudAcademy
# Diferentes lineas de codigo para ejemplificar el uso de REGEX en Python

import re

pattern = r'ab'
text = 'abc acb'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# The pattern contains a period (.), this is a character class and a period by itself will match any single character.

pattern = r'.'
text = 'abcdef'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


# The \d character class matches a single digit, you've changed the text to be searched to a string containing a single-digit between two words.

pattern = r'\d'
text = 'FirstWord 1 LastWord'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


# \D matches any non-digit characters, all characters except the digit 1 were matched. This is the opposite of \d.

pattern = r'\D'
text = 'FirstWord 1 LastWord'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


# The combination of the word character class (\w) with the plus symbol quantifier (+) will match one or more word characters. To describe that in a different way, you have matched the words in the text, ignoring the spaces between the words.

pattern = r'\w+'
text = 'FirstWord 1 LastWord'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


pattern = r'[4-6]'
text = '123456789'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


pattern = r'[4-6]+'
text = '123456789'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


pattern = r'[d-f]+'
text = 'abcdefghi'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


pattern = r'[a-z0-9]+'
text = 'word!1234?wordandletters'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


pattern = r'[^aeuio]+'
text = 'The quick brown fox jumps over the lazy dog.'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


pattern = r'[^aeuio^\s]+'
text = 'The quick brown fox jumps over the lazy dog.'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")
