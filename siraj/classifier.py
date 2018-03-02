from sklearn import tree

# Decision tree =  stores data and asks each node does it contain x or not if the x is yes the data moves one
# direction if the answer is no it will move the other

x = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39]]


y = ['male', 'female', 'female', 'female', 'male', 'male', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x, y)

prediction = clf.predict([[181, 80, 44]])

print prediction
