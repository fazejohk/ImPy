import wikipedia
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import tree
x = 0
y = 0

words = []
whatisit = []
vectorizer = CountVectorizer()
decision = tree.DecisionTreeClassifier()
# So this is what is happening:
# I'm opening a word list called SkullSecurityComp
# and searching the terms inside the word list from Wikipedia
# if it finds something it will return true and else it will return false
with open("/home/me/Downloads/SkullSecurityComp") as f:
    for line in f:
        try:
            if wikipedia.summary(line, sentences=1):
                print "True"
                lenght = len(line) - 2
                words.append(line[0:lenght])
                whatisit.append("Good")
                x += 1

        except KeyboardInterrupt:
            count = x + y
            print "\nTrue:" + str(x)
            print "False:" + str(y)
            print "Scanned:" + str(count)
            """"
            print "Words:" + str(words)
            print "What is it:" + str(whatisit)
            """
            vectorizer.fit(words)
            vector = vectorizer.transform(words)
            """
            print "Shape"
            print vector.shape
            print "Type"
            print type(vector)
            print "Toarray"
            print vector.toarray()
            """
            decision.fit(vector.toarray(), whatisit)
            userinput = ""
            while userinput != 'q':
                userinput = raw_input("Search:\n")
                text = [str(userinput)]
                vector2 = vectorizer.transform(text)
                prediction = decision.predict(vector2.toarray())
                print prediction
            exit(0)

        except:
            print "False"
            lenght = len(line) - 2
            words.append(line[0:lenght])
            whatisit.append("Bad")
            y += 1


