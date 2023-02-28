import csv
file = open("swap_data.csv")
type(file)
csvreader = csv.reader(file)
next(csvreader)
next(csvreader)
header = []
header = next(csvreader)
#print(header)
rows=[]
for row in csvreader:
    r = str(row)
    rows.append(r.split())
sumi=0
for i in range(len(rows)):
    sumi+=float(rows[i][3])
average = sumi/len(rows)
print("average load on swap =", average)
file.close()
