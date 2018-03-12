from sklearn import tree
from random import randint, choice

# Decision tree =  stores data and asks each node does it contain x or not if the x is yes the data moves one
# direction if the answer is no it will move the other
x = []
movies = {}
keys = movies.viewkeys()
values = movies.viewvalues()

with open("test.txt", 'r') as f:
    text = f.readlines()
    clones = 0
    for line in text:
        if line in keys:
            movies.update(line=movies[str(line)] + 1)
        else:
            movies[line] = 1


print movies




"""
clf = tree.DecisionTreeClassifier()

clf = clf.fit(x, y)
with open("test.txt", 'w+') as f:
    f.write(str(x) + "\n" + str(y))

prediction = clf.predict([[181, 80]])

print prediction
"""