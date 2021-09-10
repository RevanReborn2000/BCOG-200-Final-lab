import nltk
import os

""" Comment this code """
title_list = []   #here we create three lists
text_list = []
fdist_list = []
uniqueList = []
numwords = []
word_list = []
jk = 0

input_directory = 'books/'   #these two code lines access the file directory we need 
book_file_list = os.listdir(input_directory)   
for book in book_file_list:
    if book[0] == '.':  #removes any books that contain a period in their title
        book_file_list.remove(book)
    else:
        title = book[:-4]  #determines the index of the string charaters for each book title , appends each title to a list, and adds it to the file path (directory plus title)
        title_list.append(title)
        print("Importing", book)
        f = open(input_directory + book, encoding ="utf8") #opens book and reads it
        book_string = f.read()
        tokens = nltk.word_tokenize(book_string)
        text = nltk.Text(tokens)
        text_list.append(text)       #this block tokenizes each books text and appends it to a textlist, along with the frequency of its most common words, which it appends to a list.
        fdist = nltk.FreqDist(text)
        unique = set(a for a in text)
        uniqueList.append(unique)
        numwords.append(palabra for palabra in text)
        #print("the number of words in this text is: " + str(len(numwords)))
         

    
        fdist_list.append(fdist)
        print(title, fdist['human'])   #this tests all of our code. 
        print(fdist.most_common(10))
        print(nltk.FreqDist(book)) 
        #print("the number of unique words in this one are: " + str(len(uniqueList)))

        

"""
USING NLTK:
    1. create a frequency distribution nltk object for each text and store in the fdist list #you already did that?  " fdist_list.append(fdist)"????????????
    2. print out the number of total and unique words in each book       
    3. pick 10 words you are interested in and print out how many times each
        occurred in each book in a nice, organized formatted table
"""

print(fdist)

