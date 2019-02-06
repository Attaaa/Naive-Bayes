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
    for x in data:
        y = x[className]
        if (y not in new_data):
            new_data[y] = []
        new_data[y].append([x[i] for i in range(len(x)-1)])
    return new_data

def sourtoutData(data):
    data_first = {}
    for k, y in data.items():
        data_second = {}
        for row in y:
            data_convert = {}
            for i in range(1,len(row)):
                print(i)
                if (i not in data_second):
                    data_second[i] = {}
                if (row[i] in data_second[i]):
                    data_second[i][row[i]] += 1
                else:
                    data_convert[row[i]] = 1
                    data_second[i] = data_convert
                print(data_second)
        # print(data_convert)
        # data_first[k] = data_convert

    print(data_first)
            


# def average(data):
#     return sum


data_file = load_data('TrainsetTugas1ML.csv')

data_file = [data_file[i] for i in range(5)]

# print(data_file)

# data_train = [data_file[x] for x in range(10)]

# test = splitDataByClass(data_train)  

# sourtoutData(test)

# print(data_train)

