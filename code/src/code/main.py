from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import export_graphviz

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

tree.plot_tree(clf.fit(X, Y))