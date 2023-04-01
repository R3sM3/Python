import re
# pattern = r'.'
# Example text to search:
# 0987654321234567890
pattern = r'[6-8]'
text = '0987654321234567890'
# Should match:
# ['8', '7', '6', '6', '7', '8'] 
matches = re.findall(pattern, text)
print(f"{matches}")



import re
pattern = r'ho{1,2}p'
# Example text to search:
# 'hop hoop hooop hoooop hooooop'
text = 'hop hoop hooop hoooop hooooop'
# Should match:
# ['hop', 'hoop']
matches = re.findall(pattern, text)
print(f"{matches}")



import re
pattern = r'.*://(.*)'
# Example text to search:
# 'https://cloudacademy.com'
text = 'https://cloudacademy.com'
# Should match:
# ['cloudacademy.com']
matches = re.findall(pattern, text)
print(f"{matches}")


import re

pattern = r'.*(?=[0-9]).*'
# Example text to search:
text = '''
space
space1
apple
2apple
brush
brush3
'''
matches = re.findall(pattern, text, re.MULTILINE)
print(f"{matches}")
# Should match:
# ['space1', '2apple', 'brush3']



import re

pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

# Example text to search:
text = '''
user1 GET /endpoint 1.1.1.1 200
user2 POST /endpoint 2.2.2.2 201
user1 PUT /endpoint 3.3.3.3 500
user1 PATCH /endpoint 4.4.4.4 401
'''
matches = re.findall(pattern, text, re.MULTILINE)
print(f"{matches}")

# Should match:
# ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']

