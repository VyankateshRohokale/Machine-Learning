import MyKNNmodule 


def main():

    print(" ---Welcome To The Demonstration Of KNN Classification--- ")
    print("By Vyankatesh Suresh Rohokale...")
    no = int(input("Please Tell The Number Of entry's You are Doing (Atleast 5 Entry's): "))
    if no < 5:
        print("Enter more than 4 entry ..")
        exit()
    feature = []
    lable = []
    for i in range(0,no):

        print( i +1 , "Entry")

        no1 = int(input(" Theory Marks : "))
        no2 = int(input(" Practical Marks : "))
        result = input(" Result : ")
        if result.lower() == "fail":
            result = 0
        elif result.lower() == "pass":
            result = 1
        else:
            result = 1


        temp = []
        temp.append(no1)
        temp.append(no2)
        feature.append(temp)

        lable.append(result)

        
    k = int(input("Enter The Value Of K : "))

    if k > len(feature):
        print("Value of K is Greater Than The Length Of Features , do not Try To test the Code.. ;)")

    print("Features are : ",feature)
    print("Lables are : ",lable)

    toopredict = []

    toopredict.append(int(input("Enter The Theory Marks For Prediction : ")))
    toopredict.append(int(input("Enter The Practical Marks For Prediction : ")))


    ans = MyKNNmodule.KNN(feature ,  lable , k ,  toopredict)
    
    print(ans)

    print("-------------------------------------------------------------------------------------------------------")
    print("     Leetcode     -> https://leetcode.com/u/piyushrohokale2525/")
    print("      Github      -> https://github.com/VyankateshRohokale")
    print("  Email Address   -> piyushrohokale2525@gmail.com")

    print("-------------------------------------------------------------------------------------------------------")

    





if __name__ == "__main__":
    main()