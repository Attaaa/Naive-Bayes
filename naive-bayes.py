import csv
import math
import operator

def load_data(file_name):
    fileCsv = csv.reader(open(file_name), delimiter=',')
    data = list(fileCsv)
    data_dict = {}

    for x in data[0]:
        data_dict[x] = ""
    
    data = [data[i] for i in range(1,len(data))]
    data2 = []

    for x in data:
        y = 0
        for k in data_dict.keys():
            data_dict[k] = x[y]
            y += 1
        data2.append(data_dict.copy())
    
    return data2


def splitDataByClass(data, className):
    new_data = {}

    for row in data:
        y = row[className]
        if (y not in new_data):
            new_data[y] = []

        del row[className]
        new_data[y].append(row.copy())

    return new_data


def numberedData(data):
    dict1 = {}

    for className in data:
        
        dict1[className] = {}
        dict2 = {}

        for row in data[className]:
            for k in row:
                if (k != 'id'):
                    if (k not in dict2):
                        dict2[k] = {}
                    if (row[k] not in dict2[k]):
                        dict2[k][row[k]] = 1
                    else:
                        dict2[k][row[k]] += 1
            
        dict1[className] = dict2.copy()
        dict1[className]['count'] = len(data[className])

    return dict1


def getProbabilityData(data, totalData):

    data2 = {}
    data2 = data.copy()

    for className in data2:

        for attribute in data2[className]:

            if (attribute != 'count'):

                for value in data2[className][attribute]:

                    data2[className][attribute][value] /= data2[className]['count']
        
        data2[className]['prob'] = data2[className]['count'] / totalData
        del data2[className]['count']
    
    return data2


def getPrediction(data, trainSet):
    hasil = []

    for row in data:
        temp = {}

        for attr, val in row.items():

            if (attr != 'id' and attr != 'income'):

                for className in trainSet:
                    if (className not in temp):
                        temp[className] = 1

                    if (val in trainSet[className][attr]):
                        temp[className] *= trainSet[className][attr][val]

        test = max(temp.items(), key=operator.itemgetter(1))[0]
        hasil.append(test)

    return hasil
    # for x in hasil:
    #     test = "%.5f" % (x)
    #     print(test)


def trainAccuracy(data_test, data_prediction, className):
    i = 0
    trueData = 0

    for row in data_test:
        if (row[className] == data_prediction[i]):
            trueData += 1
        i += 1
    
    return trueData/len(data_prediction)


data_file = load_data( 'TrainsetTugas1ML.csv' )

totalDataTrain = 100
totalDataTest = len(data_file) - totalDataTrain

data_train = [data_file[i] for i in range( totalDataTrain )]
data_test = [data_file[i] for i in range( totalDataTrain, ( len(data_file) ) )]


data_train = splitDataByClass( data_train, "income" )  

dataNumber = numberedData( data_train )

trainSet = getProbabilityData( dataNumber, totalDataTrain )

prediction_result = getPrediction( data_test, trainSet )

accuracy = trainAccuracy( data_test, prediction_result, "income" )

print(accuracy)
