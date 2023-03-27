message1 = "Hello World"
message2 = "Desde STGO"

#CODE2: Use string concaternation then print to the console
print(message1 + " - " + message2)

#CODE3: Use string formatting and interpolation then print to the console
print("%s - %s" % (message1, message2))

#CODE4: Uppercase the message vars before printing to the console:
print("%s - %s" % (message1.upper(), message2.upper()))

#CODE5: Create an array of words and then loop over array and determine string length of each word
words = [message1, message2]
for w in words:
print(w, len(w))
