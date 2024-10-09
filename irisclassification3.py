from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    print("----- Iris Flower Classification Case Study -----")
    print("Please Enter The Features Of the Flower Below ..")

    iris = load_iris()

    print(iris)
    
    

    # print(type(data))
    features = iris.data
    labels = iris.target

    print("Features are : ")
    print(features)

    print("Labels are : ")
    print(labels)

    data_train, data_test, target_train, target_test = train_test_split(features,labels,test_size = 0.5)
    
    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(data_train,target_train)

    output = obj.predict(data_test)

    accuracy = accuracy_score(target_test,output)

    print("accuracy is : ",accuracy*100 , "%")


    print("---------------------------------------------------")

if __name__ == "__main__":
    main()