import csv

k = open("k+.csv","a")

def read_csv(csv_file):
    csv_contents = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            csv_contents.append(row)
    return csv_contents

while True:
    x = read_csv("keylog.csv")
    if x[len(x)-1::][17] + x[len(x)-1::][18]
