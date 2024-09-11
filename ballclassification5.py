from sklearn import tree

def marvellousclassifier(weight,surface):

    # Feature Encoding
    features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1]]

    # Label Encoding
    labels = [1,1,2,1,2,1,2,1,1,1]

    # Decide The Algorithm
    obj = tree.DecisionTreeClassifier()

    # Train The Mode
    obj = obj.fit(features,labels)

    ret = obj.predict([[weight,surface]])

    if ret ==1:
        print("Your object looks like tennis ball")
    else:
        print("your ball looks like cricket ball")    


def main():
    print("------ Ball Type Classification Case Study-----")
    print("PLease enter the infirmation about the object that you want to test..")
    no = int(input("Please enter the weight of your object in grams : "))
    
    print("please mention the type of surface of that object  weather it is rough os smooth : ")
    data = input()
    

    if data.lower() == "rough":
        data = 1
    elif data.lower() == "smooth":
        data = 0
    else:
        print("Invalid type of surface")
        exit()

    marvellousclassifier(no,data)

if __name__ == "__main__":
    main()

