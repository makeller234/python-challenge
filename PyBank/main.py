import os
import csv

csvpath =os.path.join("..","PyBank", "budget_data.csv")

with open(csvpath, newline='') as budgetFile:
    csvreader = csv.reader(budgetFile, delimiter=',')

    csv_header = next(csvreader)

    totalMonths = 0
    totalMoney = 0.0
    greatProfits = 0


    for row in csvreader:
        totalMonths += 1
        totalMoney += float(row[1])

#make a list an empty list of all the values outside the loop, then loop through and add to list
#and then do math outside the loo
        '''if value > greatProfits:
            greatProfits = value
        else:
            greatProfits = greatProfits'''












        

 