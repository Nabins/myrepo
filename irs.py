import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
type(iris)
x= iris.data
y= iris.target
x_20 = iris.data[0:500]
y_20 = iris.data[0:500]
knn = KNeighborsClassifier(n_neighbors= 1)
print(knn)

knn.fit(x,y)
x_new = ([3,5,4,2],[5,4,3,2])
print(knn.predict(x_new))

plt.scatter(x_20 ,y_20)
plt.show()

