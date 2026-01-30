text = "Hello World"
print(text)
text = 'Hello World 2' # single vs double
print(text)
print(text[4]) # fourth letter is o, and we begin count from zero not 1
print(len(text)) # length of the text
text = ""
print(len(text))

text = "Bob"
print(text[-1]) # last character in the string
print(text[-3])

# print(text[3]) # this is an indexerror because there is no fourth letter in Bob
print(text[6/3]) # this is = 2.0 and we cant use a float so we have to convert to integer
print(text[6//3]) # this converts // is an integer division so now its 2 not 2.0