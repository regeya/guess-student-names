import csv
import glob
import os

myfiles = glob.glob(r'''C:\Users\shane\Downloads\names\*.txt''')
unique_names = set()
surnames = set()

for myfile in myfiles:
    with open(myfile, 'r') as csvfile:
        myreader = csv.reader(csvfile)
        for row in myreader:
            unique_names.add(row[0])

with open(r'''C:\Users\shane\Downloads\Names_2010Census.csv''', 'r') as csvfile:
    myreader = csv.reader(csvfile)
    for row in myreader:
        x = row[0][0] + row[0][1:-1].lower()
        surnames.add(x)

herrin_names = []

herrin_seniors = glob.glob(r'''C:\Users\shane\Downloads\Herrin_2018_Seniors\*.jpg''')
for x in herrin_seniors:
    mystudent = os.path.basename(x)
    fn = ""
    ln = ""
    pfn = []
    pln = []
    lowered = mystudent.lower()
    for y in unique_names:
        lfn = y.lower()
        if lowered.find(lfn,0) == 0:
            pfn.append(y)
    pfn.sort(key = lambda x:len(x))
    my_fn = pfn[-1]
    my_start = len(my_fn) - 1
    for y in surnames:
        lln = y.lower()
        if lowered.find(lln, my_start) > my_start:
            pln.append(y)
    pln.sort(key = lambda x:len(x))
    my_ln = pln[-1]
    herrin_names.append([mystudent,my_fn, my_ln])

with open(r'''C:\Users\shane\Documents\herrin_names.csv''', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in herrin_names:
        csvwriter.writerow(i)