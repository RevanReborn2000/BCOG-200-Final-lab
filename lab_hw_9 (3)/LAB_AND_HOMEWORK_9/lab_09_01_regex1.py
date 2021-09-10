"""
A regex, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

Python has a built-in package called re, which can be used to work with Regular Expressions.
Go through the file and uncomment out the print statements section by section to see how regex's work.
"""

import re

some_text = "Spring is here!"
ok = "swdwdwd"
y = re.search("swd", ok) #test 
x = re.search("Spring", some_text)
if x:
	print("YES! We have a match!")
else:
	print("No match")
print()

"""
There are two things to keep track of when doing regex's in python. The first is that there are different regex 
functions:
    1. findall()
    2. search()
    3. split()
    4. sub()
"""

"""
Findall is very straightforward. It returns a list of each occurrence of the searched-for string
"""
some_text = "The rain in Spain will grow the grain."
x = re.findall("ain", some_text)
print(x)
print()

# create your own text, and add multiple words to the check list. Then write a loop that checks for each word in the 
# check list and prints out how many times the word occurs. #these directions are confusing. What does this even mean? do we add the words of the text?! or append any word we want? this method only works on strings, not lists. So why do we need a string a and a list? are we even supposed to call the re.findall method? since that was not specified, im going to do EXACTLY as the directions ask without using findall. I should not have to go to office hours for that
#some_text2 = "peter piper packed a pickled piper jar"  #  "create your own text"
#check_list = ["apple", "orange", "orange", "apple", "apple", "strawberry"] # "add multiple words to the checklist"
#check_list2 = set(check_list)
#for word in check_list2:
	#print('there are:', check_list.count(word), word , 'in the check list.')   #here's the for loop.


#MAYBE THIS IS THE SOLUTION TO THIS STRANGELY-WORDED PROBLEM? if not, the code above should suffice. 
some_text = "peter piper packed a pickled piper jar for piper pipers"
check_list = re.findall("piper",some_text)
weirdly_worded = {}
for i in check_list:
	print('there are:', check_list.count(i), "'" + str(i) + "s"+ "'" +  ' in the check list.')




	
#

"""
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned.
"""
some_text = "Spring is here!"
x = re.search("Spring", some_text)
y = re.search("Winter", some_text)
print(x)
print(y)
print()

""" 
Notice how 'None' gets returned if there is no match. If there is a match, the match object shows you the character
    positions where the string occurred. But only the first one.
"""
some_text1 = "Spring is here!"
some_text2 = "Finally, Spring is here!"
some_text3 = "It is Spring Spring Spring"
x = re.search("Spring", some_text1)
y = re.search("Spring", some_text2)
z = re.search("Spring", some_text3)
print(x)
print(y)
print(z)
print()

"""
You can access those values directly by calling the start() and end() methods on the match object.
"""
some_text1 = "Spring is here!"
x = re.search("Spring", some_text1)
print(x.start(), x.end())
print()

# say you wanted to get a list of the character positions of all occurrences of a search string within some larger
# string. How would you do that? Write code that does it and prints them all out. 


lista = []
largerstring = "i like to eat i like to eat i like like to to to to eat"
for a in re.finditer("like", largerstring):
	lista.append(a.span())
print("The positions of the chosen word within the larger string are as follows: " + str(lista))


"""
The split function you already have some experience with, as it can be used directly on a string without importing re.
But within re it has more options which we will learn about later. To use 'split' the 're' way, you pass it two
arguments, the split character(s), and then the string you want to split.
"""
some_text = "here is a comma separated list, apple, orange, banana"
x = re.split(',', some_text)
print(x)  

"""
The sub function does substitutions. Think 'find-replace'. 
"""
some_text3 = "It is Spring Spring Spring"
x = re.sub("Spring", "Summer", some_text3)
print(x)