import csv
file = open("memory_data.csv")

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
    sumi+=float(rows[i][4])
average = sumi/len(rows)
print("average load on memory = ", average)
file.close()
x = open("memory_average.txt",'w')
x.write(str(average))
x.close()
