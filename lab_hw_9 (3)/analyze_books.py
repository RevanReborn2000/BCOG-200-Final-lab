# Write a program called "analyze_books.py"
    #   - in it, create a class called "Book". The class should have attributes and methods appropriate for doing the
    #       the following: -DONE
    #   - storing the tokenized, lower-cased text of all the words in the book (1 pt) -DONE
    #   - storing a version of the text with stop words removed (1 pt) -DONE
    #   - storing a list of each word's part of speech (POS). For example, if the raw text list was
    #       "['the', 'dog', 'runs'", the POS list would be "[('the', 'DT'), ('dog', 'NN'), ('runs', 'NNS')]" (1 pt) -DONE 
    #   - Uses NLTK's FreqDist() to get word frequency distributions for the book, and print out the number of unique
    #       and total words (1 pt) -DONE
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

import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import os.path

class Book:
    def __init__(self,title):
        self.title = title
        self.read = None
        self.tokenized_lowered_list = None
        self.tagged_list = None
        self.freqs = None

    def read_book(self,title):
        f = open("my_books/" + title, "r")
        self.read = f.read()
        return self.read
        f.close()

    def lower_case_tokener(self,read):
        self.tokenized_lowered_list = []
        tokens = nltk.word_tokenize(read)
        text = nltk.Text(tokens)
        for word in text:
            x = word.split(" ")
            for word in x:
                a = word.lower()
                a = a.strip("(")
                a = a.strip(")")
                a = a.strip("--")
                a = a.strip(".")
                a = a.strip(",")
                a = a.strip("/")
                a = a.strip(".")
                a = a.strip("//")
                a = a.strip("!")
                a = a.strip(":")
                a = a.strip(";")
                a = a.strip("''")
                a = a.strip("?")
                self.tokenized_lowered_list.append(a)
                #print(self.tokenized_lowered_list) please uncomment this if you want to test the code. The next two functions use it so it obviously works, but my pc is slow and the runtime is awful.
        return self.tokenized_lowered_list #will include some weird " "" " inside of the text. Would not let me remove. 

    def stop_words(self, read_text):
        tokens_text = nltk.word_tokenize(read_text)
        texter = str(nltk.Text(tokens_text))
        stop_words = set(stopwords.words('english')) 
        word_tokens = word_tokenize(texter) 
        filtered_sentence = [w for w in word_tokens if not w in stop_words] 
        filtered_sentence = [] 
        for w in word_tokens: 
            if w not in stop_words: 
                filtered_sentence.append(w) 
        print((filtered_sentence)) #using "english" as the argument for the stopwords method reduces the text to 12 words. Using that module, it effectively removes stopwords, but maybe too many stopwords. 
    
    def pos_tag(self,tokenized_lowered_list):
        newstring = " "
        newstringer = newstring.join(tokenized_lowered_list)
        newstringers = nltk.word_tokenize(newstringer)
        self.tagged_list = nltk.pos_tag(newstringers)
        print(self.tagged_list[0:50]) #This is printing too much, feel free to adjust the range to check if the code works completely

    def unique_word_freq_dist(self,text):
        self.freqs = nltk.FreqDist(text)
        q = dict((word, freq) for word, freq in self.freqs.items() if not word.isdigit())
        #print(q) prints out the total word frequency, but prints out alot. Feel free to uncomment to test if code actually works.
        print("Total number of words: " +  str(len(self.freqs))) #total number of  words   
        print("Total number of unique words: " + str(len(q))) #total number of unique words

    def grammar_frequency(self, tagged_list, book_name):
        Nouns_dict = {}
        Nouns_list = []
        Verbs_dict = {}
        Verbs_list = []
        Adjectives_Dict = {}
        Adjectives_list = []
        for i in self.tagged_list:
            if i[1] == "NN":
                Nouns_list.append(i[0])
            elif i[1] == "VB":
                Verbs_list.append(i[0])
            elif i[1] == "JJ":
                Adjectives_list.append(i[0])

        Nouner = nltk.FreqDist(Nouns_list)
        Nouns_freq_list = Nouner.most_common(10)
        
        Verber = nltk.FreqDist(Verbs_list)
        Verbs_freq_list = Verber.most_common(10)

        Adjectiver = nltk.FreqDist(Adjectives_list)
        Adjectives_freq_list = Adjectiver.most_common(10)
        
        #This block takes the ten most common words and strips away the numbers next to them from the Freqdist method. It then adds it to the proper dictionary. 
        Nouns_freq_list2 = []
        for noun in Nouns_freq_list:
            nounie = noun[0]
            Nouns_freq_list2.append(nounie)
        
        
        Verbs_freq_list2 = []
        for verb in Verbs_freq_list:
            verbie = verb[0]
            Verbs_freq_list2.append(verbie)
        
        Adjectives_freq_list2 = []
        for adjective in Adjectives_freq_list:
            adjectivie = adjective[0]
            Adjectives_freq_list2.append(adjectivie)
        


        print(book_name)
            
        Nountogether = ", "
        Nountogther2 = Nountogether.join(Nouns_freq_list2)
        print("     Nouns: " + Nountogther2)

        Verbtogether = ", "
        Verbtogether2 = Verbtogether.join(Verbs_freq_list2)
        print("     Verbs: " + Verbtogether2)


        AdjectiveTogether = ", "
        AdjectiveTogether2 = AdjectiveTogether.join(Adjectives_freq_list2)
        print("     Adjectives: " + AdjectiveTogether2)

        
def main():
    folder = "my_books/"
    for filename in os.listdir(folder):
        bookObject = Book(filename.strip(".txt"))
        xim = bookObject.read_book(filename)
        xoxo = bookObject.lower_case_tokener(bookObject.read_book(filename))
        xaxa = bookObject.stop_words(bookObject.read_book(filename))
        xexe = bookObject.pos_tag(xoxo)
        xyxy = bookObject.unique_word_freq_dist(xoxo)
        xidxid = bookObject.grammar_frequency(xexe, filename.strip(".txt").upper())


main()
