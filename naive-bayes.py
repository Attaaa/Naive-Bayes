import csv
import math

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
        


def splitDataByClass(data,className):
    new_data = {}
    for row in data:
        y = row[className]
        if (y not in new_data):
            new_data[y] = []

        del row[className]
        new_data[y].append(row.copy())

    return new_data


def numberedData(data):
    dict2 = {}
    dict1 = {}

    for className in data:
        
        dict1[className] = {}
        temp = data[className]

        for row in temp:
            for k in row:
                if (k != 'id'):
                    if (k not in dict2):
                        dict2[k] = {}
                    if (row[k] not in dict2[k]):
                        dict2[k][row[k]] = 1
                    else:
                        dict2[k][row[k]] += 1
            
        dict1[className] = dict2.copy()

    return dict1



data_file = load_data('TrainsetTugas1ML.csv')

data_file = [data_file[i] for i in range(5)]

# print(data_file)

# data_train = [data_file[x] for x in range(10)]

test = splitDataByClass(data_file,"income")  

numberedData(test)

# print(data_train)

