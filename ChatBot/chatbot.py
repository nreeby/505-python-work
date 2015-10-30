#run this line before running code
#$ pip install wikipedia
#if this dosn't work
#manuel download then run (python setup.py install --user) from downloaded folder 
#also you need to run (python -W ignore(file position))
stopwords = set(("a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "name", "no", "nor", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "called", "feeling", "thank", "thanks", "pretty", "call", "kind", "just", "that's"))
stop = set(stopwords)
import wikipedia
import os

def search():
    os.system("say 'What do you think of that? '") 
    searchs=raw_input("What do you think of that? ")
    searchs=searchs.lower()
    searchsWords = searchs.split()
    for searchsword in reversed(searchsWords):
        if searchsword in stop:
            searchsWords.remove(searchsword)
    os.system("say 'Did you know that '")
    os.system("say " + searchsWords[0])
    os.system("say ' is;'")
    print("Did you know that " + searchsWords[0] + " is;")  
    print wikipedia.summary(searchsWords[0])
    search()
def Positive():
    os.system("say 'That is good to hear!! But can you tell me why? '") 
    searchGood=raw_input("That is good to hear!! But can you tell me why? ")
    searchGood=searchGood.lower()
    searchGoodWords = searchGood.split()
    for goodword in reversed(searchGoodWords):
        if goodword in stop:
            searchGoodWords.remove(goodword)
    os.system("say 'Did you know that '")
    os.system("say " + searchGoodWords[0])
    os.system("say ' is;'")
    print("Did you know that " + searchGoodWords[0] + " is;") 
    print wikipedia.summary(searchGoodWords[0])
    search()
def Negative():
    os.system("say 'Well, that sucks!!! Why is that? '") 
    searchBad=raw_input("Well, that sucks!!! Why is that? ")
    searchBad=searchBad.lower()
    searchBadWords = searchBad.split()
    for badword in reversed(searchBadWords):
        if badword in stop:
            searchBadWords.remove(badword)
    os.system("say 'Did you know that '")
    os.system("say " + searchBadWords[0])
    os.system("say ' is;'")
    print("Did you know that " + searchBadWords[0] + " is;")
    print wikipedia.summary(searchBadWords[0])
    search()
def Hello():
    os.system("say 'hello'") 
    raw_input("Hello ")
    os.system("say 'What do I call a Hansome Devil like yourself? '")
    HI= raw_input("What do I call a Hansome Devil like yourself? ")
    HI=HI.lower()
    HIWords = HI.split()
    for word in reversed(HIWords):
        if word in stop:
            HIWords.remove(word)
    HI=''.join(HIWords)
    os.system("say 'Hi,'")
    os.system("say " + HI)
    os.system("say 'How are you? '")
    Feels=raw_input("Hi " + HI + " ,How are you? ") 
    Feels=Feels.lower()
    FeelsWords = Feels.split()
    for feelword in reversed(FeelsWords):
        if feelword in stop:
            FeelsWords.remove(feelword)
    Feels=''.join(FeelsWords)
    if Feels in ["good", "great", "fantastic", "awesome", "incredible", "excellent", "fine"] :
        Positive()
    elif Feels in ["notgood", "bad", "sad", "mad", "lonely", "angry", "ill"] :
        Negative()
    else:
        os.system("say 'Is there a particular reason why? '")
        searchNeautral=raw_input("Is there a particular reason why?")
        searchNeautral=searchNeautral.lower()
        searchNeautralWords = searchNeautral.split()
        for neutralword in reversed(searchNeautralWords):
            if neutralword in stop:
                searchNeautralWords.remove(neutralword)
        os.system("say 'Did you know that '")
        os.system("say " + searchNeautralWords[0])
        os.system("say ' is;'")
        print("Did you know that " + searchNeautralWords[0] + " is;") 
        print wikipedia.summary(searchNeautralWords[0])
        search()
Hello()