from sklearn import tree


# Rough 1
# Smooth 0 
# Tennis 1
# Cricket 2
def main():

    print("Ball Classification Case Study...")

    # Feature Encoding
    features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1]]

    # Label Encoding
    labels = [1,1,2,1,2,1,2,1,1,1]

    # Decide The Algorithm
    obj = tree.DecisionTreeClassifier()

    # Train The Mode
    obj = obj.fit(features,labels)

    # Test The Model
    print(obj.predict([[96,0]]))
    print(obj.predict([[43,1]]))    

if __name__ == "__main__":
    main()


# Dataset Size : 15
# Training Size : 10
# Testing Size :    