
def q1():
    print("Question 1 (1 Points)")
    # According to the readings for this week, what is the field of natural language processing, and what are some
    # of it's primary goals or problems that it is used to solve?
    your_answer = "Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data. "
    print(your_answer)


def q2():
    print("Question 2 (1 Points)")
    # Describe a psychological question or issue that involves language that you find interesting, and describe how
    # you might use natural language processing techniques to solve it.
    your_answer = "A nice issue is the way different languages work. How is it that I could speak a sci-fi language to a child for years and they'd grow up to understand it? Perhaps computers with info on that language could be stored and used to process foreign or new languages?  "
    print(your_answe r)


def q3():
    print("Question 3 (1 Points)")
    # According to the readings for this week, what are the some of the differences between rule-based and
    # statistical natural language processing?
    your_answer = "Systems based on automatically learning the rules can be made more accurate simply by supplying more input data. However, systems based on handwritten rules can only be made more accurate by increasing the complexity of the rules, which is a much more difficult task. In particular, there is a limit to the complexity of systems based on handcrafted rules, beyond which the systems become more and more unmanageable. However, creating more data to input to machine-learning systems simply requires a corresponding increase in the number of man-hours worked, generally without significant increases in the complexity of the annotation process."
    print(your_answer)


def q4():
    print("Question 3 (2 Points)")
    # List three differences between re.search() and re.findall()
    your_answer = "They're very simmilar. Generally speaking, search finds a single match while findall finds all matches in a string. Findall returns matched substrings, while search returns a match object. When you call group() on the match object, it returns the substring that matches the entire regex regardless of capture groups ,unlike findall.   "
    print(your_answer)


def q5():
    print("Question 5 (2 Points)")
    # Explain this code
    # import re
    # fh = open("simpsons_phone_book.txt")  #opening a text
    # for line in fh:
    #     if re.search(r"J.*Neu", line):  #checking to see if the phrase is present in any of the texts lines, and if so, print out that line stripped of any spaces. Afterward, closes the file.  
    #         print(line.rstrip())
    # fh.close()
    your_answer = "opening a text then checking to see if the phrase is present in any of the texts lines, and if so, print out that line stripped of any spaces. Afterward, closes the file.  "
    print(your_answer)


def q6():
    print("Question 6 (2 Points)")
    # What is a "stop word", and how can you use NLTK to remove stop words from an NLTK text document?
    your_answer = "A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query. See below example taken from google for second part."
    print(your_answer)


'''
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
example_sent = "This is a sample sentence, showing off the stop words filtration."
  
stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(example_sent) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
        '''
  


def q7():
    print("Question 7 (2 Points)")
    # Write a program called "get_books.py" that
    #   - Imports five books of your choice from project gutenberg, using the code from lab_09_03_try_nltk.py, and saves
    #   - each book as a text file in a folder called "my_books"
    # this program does not need to use classes, but it should have a main function that calls other functions that
    # each do specific, independent parts of the program #why would i need multiple functions just to import the books and save them?

def q8():
    print("Question 8 (9 Points)")
    # Write a program called "analyze_books.py"
    #   - in it, create a class called "Book". The class should have attributes and methods appropriate for doing the
    #       the following:
    #   - storing the tokenized, lower-cased text of all the words in the book (1 pt)
    #   - storing a version of the text with stop words removed (1 pt)
    #   - storing a list of each word's part of speech (POS). For example, if the raw text list was
    #       "['the', 'dog', 'runs'", the POS list would be "[('the', 'DT'), ('dog', 'NN'), ('runs', 'NNS')]" (1 pt)
    #   - Uses NLTK's FreqDist() to get word frequency distributions for the book, and print out the number of unique
    #       and total words (1 pt)
    #   - find and prints out the 10 most frequent nouns, verbs, and adjectives in each book, looking like this: (2 pts)
    #       MOBY DICK
    #           Nouns: whale, boat, ocean, ...
    #           Verbs: chase, fish, sail, ...
    #           Adjectives: white, wet, big, ...
    #       ALICE IN WONDERLAND
    #           Nouns: rabbit, boat, ocean, ...
    #           Verbs: drink, eat, sail, ...
    #           Adjectives: white, wet, big, ...
    #   - the program should have a main function which looks in your 'my_books' folder from the previous question,
    #       gets the list of books, loops through them and creates a Book() instance for each book, and calls each
    #       of the functions described above for each book (3 pts)
    your_answer = ""
    print(your_answer)


def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()

main()