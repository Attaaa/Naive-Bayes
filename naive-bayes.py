import csv

def load_data(file_name):
    fileCsv = csv.reader(open(file_name), delimiter=',')
    return list(fileCsv)

def splitDataByClass(data):
    new_data = {}
    for i in range(1,len(data)):
        row = data[i]
        if (row[-1] not in new_data):
            new_data[row[-1]] = 0
            print(row[-1])
        new_data[row[-1]] += 1
    return new_data


data_file = load_data('TrainsetTugas1ML.csv')
test = splitDataByClass(data_file)
print(test)

