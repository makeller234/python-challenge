import os
import csv

csvpath =os.path.join("..","PyBank", "budget_data.csv")

with open(csvpath, newline='') as budgetFile:
    csvreader = csv.reader(budgetFile, delimiter=',')

    csv_header = next(csvreader)

    totalMonths = 0
    totalMoney = 0.0
    


    values = []
    monies = 0
    for row in csvreader:
        totalMoney += float(row[1])
        totalMonths += 1
        values.append(row[1])
    totalMoney = "{:.0f}".format(totalMoney)
        
    # finding average profit/loss
    for item in values[::-1]:
        a = len(values)-1
        
        for item1 in values:
            monies = float(item)
            monies = monies -float(values[a])
            a-=1
            averageProfLoss = "{:.2f}".format(monies/(totalMonths-1))
        break

    #finding greatest decrease in profits
    money = float(item) 
    greatDecr = 0.0
    greatIncr = 0
    a = 0
    for item2 in values[::-1]:
        if money-float(values[a-1]) < greatDecr:
            greatDecr = money-float(values[a-1])
        else:
            greatDecr = greatDecr


        if money-float(values[a-1])> greatIncr:
            greatIncr = money-float(values[a-1])
        else:
            greatIncr = greatIncr

        a-=1
        money = float(values[a])
    greatDecr = "{:.0f}".format(greatDecr)
    greatIncr = "{:.0f}".format(greatIncr)














        

 