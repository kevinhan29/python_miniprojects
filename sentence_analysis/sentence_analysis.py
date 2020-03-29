'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.

**Note**: ignore all spaces.

Example input:
```
I love to work with dictionaries!
```

Example output:
```
Upper case: 1
Lower case: 26
Punctuation: 1
Total chars: 28
```
'''

# user input sentence
sentence = input("Enter any sentence: ")

# remove spaces from user input
sentence = sentence.replace(" ","")
#print(sentence)

# return number of lower case letters
num_lower = 0               # counter for lower case characters
for x in sentence:          # iterate through each character in the sentence
    if x.islower():         # check to see if the letter is lowercase
        num_lower += 1      # if it is lowercase, then add one to the counter
#print(num_lower)

# return number of upper case letters
num_upper = 0               # counter for upper case characters
for x in sentence:          # iterate through each character in the sentence
    if x.isupper():         # check to see if the letter is uppercase
        num_upper += 1      # if it is uppercase, then add one to the counter
#print(num_upper)

# return number of punctuation characters
num_punc = 0                # counter for punctuation characters
for x in sentence:
    if not x.isalnum():     # check to see if the char is an alphanumeric char
        num_punc += 1        # if it's not alphanumeric, then it's a punctuation character, add to counter
#print(num_punc)

# return total number of characters
length = len(sentence)
#print(length)

# store each of the above values in dictionary
sentence_analysis = {"Lower Case": num_lower, \
    "Uppser Case": num_upper, \
    "Punctuation": num_punc, \
    "Total Characters": length}

# output result
for x in sentence_analysis:
    print(x, ": ", sentence_analysis[x], sep="")