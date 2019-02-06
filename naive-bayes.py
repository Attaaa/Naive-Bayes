import csv

def load_data(file_name):
    fileCsv = csv.reader(open(file_name), delimiter=',')
    return list(fileCsv)

data_file = load_data('TrainsetTugas1ML.csv')
print(data_file)

