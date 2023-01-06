import csv
import datetime


def read_csv(csv_file):
    csv_contents = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            csv_contents.append(row)
    return csv_contents

x = read_csv("keylog.csv")
k = open("k+.csv","a")
print(x)

invalid_t = []

nek = 0


for i in range(6):
    invalid_t.append(f"0:00:0{i}")

for i in range(len(x)):
    if len(x) == i+2:
        break
    y = int(x[i][0][:4])
    m = int(x[i][0][5:7])
    d = int(x[i][0][8:10])
    h = int(x[i][0][11:13])
    min = int(x[i][0][14:16])
    s = int(x[i][0][17:20])

    y2 = int(x[i+1][0][:4])
    m2 = int(x[i+1][0][5:7])
    d2 = int(x[i+1][0][8:10])
    h2 = int(x[i+1][0][11:13])
    min2 = int(x[i+1][0][14:16])
    s2 = int(x[i+1][0][17:20])

    current_dt = datetime.datetime(y,m,d,h,min,s)
    future_dt = datetime.datetime(y2,m2,d2,h2,min2,s2)
    difference = future_dt - current_dt
    print(difference)

    h = open("k+.csv","r")

    if str(difference) in invalid_t and h.read(1) == "" and nek !=1:
        nek +=1
        k.write(x[i][0])
    elif str(difference) in invalid_t:
        k.write(f"{x[i][0][24:]}")
    else:
        k.write(f"\n{x[i][0]}")

    if x[i][0] == x[::-1][0]:



