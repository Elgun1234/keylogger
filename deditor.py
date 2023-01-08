class edit():
    def __init__(self):
        import csv
        import datetime
        import os

        if os.path.exists("keylog.csv") == False:
            op = open("keylog.csv", "x")

        if os.path.exists("k+.csv") == False:
            op = open("k+.csv", "x")



        def read_csv(csv_file):
            csv_contents = []
            with open(csv_file) as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for row in reader:
                    csv_contents.append(row)
            return csv_contents

        x = read_csv("keylog.csv")
        k = open("k+.csv","a")
        z = open("keylog.csv", "r")


        valid_t = []
        valid_time = 5




        for i in range(valid_time+1):
            valid_t.append(f"0:00:0{i}")
        i = 0
        valid = True


        while valid:

            if z.read(1) == "":
                while z.read(1) == "":
                    x = read_csv("keylog.csv")

                    pass

            elif x[i][0] == x[-1][0]:

                while x[i][0] == x[-1][0]:
                    x = read_csv("keylog.csv")

                    pass
            elif x[i][0] != x[-1][0]:

                y = int(x[i][0][:4])
                m = int(x[i][0][5:7])
                d = int(x[i][0][8:10])
                h = int(x[i][0][11:13])
                min = int(x[i][0][14:16])
                s = int(x[i][0][17:20])

                y2 = int(x[i-1][0][:4])
                m2 = int(x[i-1][0][5:7])
                d2 = int(x[i-1][0][8:10])
                h2 = int(x[i-1][0][11:13])
                min2 = int(x[i-1][0][14:16])
                s2 = int(x[i+-1][0][17:20])

                current_dt = datetime.datetime(y,m,d,h,min,s)
                past_dt = datetime.datetime(y2,m2,d2,h2,min2,s2)
                difference = current_dt - past_dt

                h = open("k+.csv", "r")

                if h.read(1) == "":
                    k.write(x[i][0])

                elif str(difference) in valid_t:
                    k.write(f"{x[i][0][24:]}")
                else:
                    k.write(f"\n{x[i][0]}")
                i += 1
                k.flush()



if __name__ == "__main__":
    d = edit()



