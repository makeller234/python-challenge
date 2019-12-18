import os
import csv

csvpath =os.path.join("..","PyBank", "budget_data.csv")

with open(csvpath, newline='') as budgetFile:
    csvreader = csv.reader(budgetFile, delimiter=',')

    csv_header = next(csvreader)

    totalMonths = 0
    totalMoney = 0.0
    

    #data= {}
    values = []
    monies = 0
    for row in csvreader:
        totalMoney += float(row[1])
        totalMonths += 1
        values.append(row[1])
        #data = {row[0]:row[1] for row in csvreader}

    
    for item in values[::-1]:
        a = len(values)-1
        
        for item1 in values:
            monies = float(item)
            monies = monies -float(values[a])
            a-=1
            averageProfLoss = "{:.2f}".format(monies/(totalMonths-1))
        break

    money = float(item)  #money doens't change, so this needs to be moved and/or updated somehow
    dec = 0 #money - float(values[a-1])
    a = 0
    for item2 in values:

        print(f'{a} loops money= {money}')
        if money-float(values[a-1]) < dec:
            dec = money-float(values[a-1])
        else:
            dec = dec
        a+=1


 
    #print(averageProfLoss)
    #print("{:.0f}".format(totalMoney))
    #print(totalMonths)


    

        

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













        

 