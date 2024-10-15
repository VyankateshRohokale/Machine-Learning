from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def main():
    print("----- Iris Flower Classification Case Study -----")
    print("Please Enter The Features Of the Flower Below ..")

    iris = load_iris()

    print(iris)
    

    # print(type(data))
    features = iris.data
    labels = iris.target

    print("Ffeatures are : ")
    print(features)

    print("Labels are : ")
    print(labels)

    data_train, data_test, target_train, target_test = train_test_split(features,labels,test_size = 0.5)

    print("---------------------------------------------------")

if __name__ == "__main__":
    main()