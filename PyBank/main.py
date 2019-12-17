import os
import csv

csvpath =os.path.join("..","PyBank", "budget_data.csv")

with open(csvpath, newline='') as budgetFile:
    csvreader = csv.reader(budgetFile, delimiter=',')

    csv_header = next(csvreader)

    totalMonths = 0
    totalMoney = 0.0
    

    data= {}
    values = []
    monies = 0
    for row in csvreader:
        totalMoney += float(row[1])
        totalMonths += 1
        values.append(row[1])
        #data = {row[0]:row[1] for row in csvreader}
        

    
    for item in values[::-1]:
        a = len(values)-1

        monies = float(item)
        monies = monies -float(values[a])
        a-=1
        averageProfLoss = monies/(totalMonths-1)
    print(averageProfLoss)


    

        

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













        

 