import os
import csv

csvpath =os.path.join("..","PyBank", "budget_data.csv")

with open(csvpath, newline='') as budgetFile:
    csvreader = csv.reader(budgetFile, delimiter=',')

    csv_header = next(csvreader)

    totalMonths = 0
    totalMoney = 0.0

    data= []


    for row in csvreader:
        data.append(row)
        totalMonths += 1
        totalMoney += float(row[1])

        for x in data:
            greatProfits = x[2]
            

'''
for x in data:
    totalMonths +=1
    totalMoney += float(x[1])

    greatProfits = float(x[1])
    if float(x[1])>:
        greatProfits = float(x[2][1])-float(x[1])
    else:
        greatProfits = greatProfits
'''












        

 