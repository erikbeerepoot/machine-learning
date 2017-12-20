import csv


def read_points(file):
    X = []
    Y = []
    with open(file) as csvfile:
        datareader = csv.reader(csvfile,delimiter=',')
        for row in datareader:
            X.append(float(row[0]))
            Y.append(float(row[1]))

    return X,Y