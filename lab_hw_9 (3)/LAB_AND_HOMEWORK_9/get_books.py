# Write a program called "get_books.py" that
    #   - Imports five books of your choice from project gutenberg, using the code from lab_09_03_try_nltk.py, and saves
    #   - each book as a text file in a folder called "my_books"
    # this program does not need to use classes, but it should have a main function that calls other functions that
    # each do specific, independent parts of the program #why would i need multiple functions just to import the books and save them? Maybe this comment was meant for homework question 8? (John confirmed over zoom)





from urllib import request
import os.path
import nltk




urlList = ["https://www.gutenberg.org/files/140/140-0.txt",
"https://www.gutenberg.org/files/205/205-0.txt" ,
"https://www.gutenberg.org/files/25344/25344-0.txt",
"http://www.gutenberg.org/cache/epub/7142/pg7142.txt",
"http://www.gutenberg.org/cache/epub/1254/pg1254.txt"]

titleList = ["Jungle", "Walden", "Scarlett Letter", "Sparta", "Cyrano"]

if not os.path.exists("my_books"):
	os.makedirs("my_books", 0o755)


tokenizedList =[]
for i in range(len(urlList)):
	#BOOK 1 CODE
	response1 = request.urlopen(urlList[i])
	openBook = response1.read().decode('utf8')
	openBook = openBook.strip("\ufeff")
	#print(openBook)
	text_file1 = open( "my_books/" + titleList[i]   + ".txt", "w")
	text_file1.write(openBook)
	text_file1.close()

print()
'''tokener = nltk.word_tokenize(openBook)
	to_text = nltk.Text(tokener)
	tokenizedList.append(to_text)
	print(len(openBook))
	print(to_text[0:20])
	print(text_file1)'''





	




