# ──────────────────────────────────────────────────────────────────────────────
# Exercise 1: Write a while loop that starts at the last character in the string
# and works its way backwards to the first character in the string, printing
# each letter on a separate line, except backwards.
# ──────────────────────────────────────────────────────────────────────────────
'''
thestring = input("Enter something:")
the_string = str(thestring)
lengthofstring = len(the_string) - 1

while lengthofstring > -1:
    letter = the_string[lengthofstring]
    print(letter)
    lengthofstring = lengthofstring - 1
'''
# ──────────────────────────────────────────────────────────────────────────────
# Exercise 2: Given that fruit is a string, what does fruit[:] mean?
# ──────────────────────────────────────────────────────────────────────────────
'''
fruit = 'banana'
print(fruit[:]) # It prints the entire string
'''
# ──────────────────────────────────────────────────────────────────────────────
# Exercise 3: Encapsulate this code in a function named count, and generalize it
# so that it accepts the string and the letter as arguments.
# ──────────────────────────────────────────────────────────────────────────────
'''
wordinput = input("Type a word: ")
theword = str(wordinput)
letterinput = input("Type a letter from in that word: ")
theletter = str(letterinput)

def count(word, lettertofind):
    count = 0
    for letter in word:
        if letter == lettertofind :
            count = count + 1
    print(count)

count(theword,theletter)
'''
# ──────────────────────────────────────────────────────────────────────────────
# Exercise 4: There is a string method called count that is similar to the
# function in the previous exercise. Read the documentation of this method at
# https://docs.python.org/3/library/stdtypes.html#string-methods
# Write an invocation that counts the number of times the letter "a" occurs in
# the word "banana".
# ──────────────────────────────────────────────────────────────────────────────
'''
word = 'banana'
print(word)
print(word.count('a'))
'''
# ──────────────────────────────────────────────────────────────────────────────
# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted string
# into a floating point number.
# ──────────────────────────────────────────────────────────────────────────────
'''
str = 'X-DSPAM-Confidence: 0.8475'
colonpos = str.find(':')
print(colonpos)
float_num = float(str[colonpos+2:len(str)])
print(float_num)
'''
# ──────────────────────────────────────────────────────────────────────────────
# Exercise 6: Read the documentation of the string methods at
# https://docs.python.org/3/library/stdtypes.html#string-methods
# You might want to experiment with some of them to make sure you understand
# how they work. Strip and replace are particularly useful.
# The documentation uses a syntax that might be confusing. For example, in
# find([sub[,start[, end]]) the brackets indicate optional arguments. So sub is
# required, but start is optional, and if you include start, then end is optional.
# ──────────────────────────────────────────────────────────────────────────────

# for my practice/ example I will strip all of the z's from the sentence and then 
# replace the a's with i's
'''
yeet = '#************** the word banana would be so much funnier spelled like this ************##########'
print(yeet)
no_more_z = yeet.strip('*# ')
print(no_more_z)
a_to_i = no_more_z.replace('a','i')
print(a_to_i)
'''