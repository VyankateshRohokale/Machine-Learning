
import pandas as pd 
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

input_path = "D:\\"
output_path = "D:\\"

headers = ["CodeNumber","ClumpThickness","UniformityCellSize","UniformityCellShape","MarginalAdhesion","SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses","CancerType"]


def read_data(path):

    data = pd.read_csv(path)
    return data

def get_headers(dataset):

    return dataset.columns.values


def add_headers(dataset,headers):

    dataset.columns = headers
    return dataset

def data_file_to_csv():

    headers = ["CodeNumber","ClumpThickness","UniformityCellSize","UniformityCellShape","MarginalAdhesion","SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses","CancerType"]

    dataset = read_data(input_path)

    dataset = add_headers(dataset,headers)

    dataset.to_csv(output_path,index = False)

    print("File Saved...!")


def split_dataset(dataset,train_percentage,feature_headers,target_header):

    train_x, test_x,train_y,test_y = train_test_split(dataset[feature_headers],dataset[target_header],train_size = train_percentage)

    return train_x,test_x,train_y,test_y

def handel_missing_values(dataset,missing_values_header,missing_label):
    return dataset[dataset[missing_values_header] != missing_label]


def random_forest_classifier(features, target):

    clf = RandomForestClassifier()
    clf.fit(features,targetr)
    return clf

def dataset_statistics(dataset):
    print(dataset.descibe())

def main():
    dataset = pd.read_csv(output_path)

    dataset_statistics(dataset)

    dataset = handle_missing_values(dataset, headers[6],'?')

    train_x,test_x,train_y,test_y = split_dataset(dataset,0.7,headers[1:-1],headers[-1])

    print("Train_x shape :: ", train_x.shape)
    print("Train_x shape :: ", train_y.shape)
    print("test_x shape :: ", test_x.shape)
    print("test_x shape :: ", test_y.shape)

    trained_model = random_forest_classifier(train_x, train_y)

    print("Trained Model :: ", trained_model)

    predictions = trained_model.predict(test_x)

    for i in range(0,205):
        print("Actual outcome :: {} and predicted outcome :: {}".format(list(test_y)[i],predictions[i]))


    print("Train Accuracy :: ",accuracy_score(train_y,trained_model.predict(train_x)))
    print("Test Accuracy :: ", accuracy_score(test_y,predictions))
    print("Confusion matrix ", confusion_matrix(test_y),predictions)


if __name__ == "__main__":
    main()