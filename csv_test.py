import csv
filename = 'FreePeriodList.csv'
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
rowdata=[]
i=0
with open (filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if(row[3]) == 'A':
            print (row[1])
            A.append(row)
        elif(row[3]) == 'B':
            print (row[1])
            B.append(row)
        elif(row[3]) == 'C':
            print (row[1])
            C.append(row)
        elif(row[3]) == 'D':
            print (row[1])
            D.append(row)
        elif(row[3]) == 'E':
            print (row[1])
            E.append(row)
        elif(row[3]) == 'F':
            print (row[1])
            F.append(row)
        elif(row[3]) == 'G':
            print (row[1])
            G.append(row)

    