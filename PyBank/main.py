import os
import csv

csvpath =os.path.join("..","PyBank", "budget_data.csv")

with open(csvpath, newline='') as budgetFile:
    csvreader = csv.reader(budgetFile, delimiter=',')
    csv_header = next(csvreader)

    totalMonths = 0
    totalMoney = 0.0
    values = []
    dates = []
    monies = 0

    for row in csvreader:
        totalMoney += float(row[1])
        totalMonths += 1
        values.append(row[1])
        dates.append(row[0])
    
    # finding average profit/loss
    for item in values[::-1]:
        a = len(values)-1
        
        for item1 in values:
            monies = float(item)
            monies = monies -float(values[a])
            a-=1
            averageProfLoss = "{:.2f}".format(monies/(totalMonths-1))
        break

    #finding greatest decrease and increase in profits
    money = float(item) 
    greatDecr = 0.0
    greatIncr = 0
    a = 0

    for item2 in values[::-1]:
        if money-float(values[a-1]) < greatDecr:
            greatDecr = money-float(values[a-1])
        else:
            greatDecr = greatDecr
        
        if greatDecr==money-float(values[a-1]):
            greatDecrMonth=dates[a]

        if money-float(values[a-1])> greatIncr:
            greatIncr = money-float(values[a-1])
        else:
            greatIncr = greatIncr
                
        if greatIncr == money-float(values[a-1]):
            greatIncrMonth = dates[(a)]
            
        a-=1
        money = float(values[a])

    #format variables
    totalMoney = "{:.0f}".format(totalMoney)
    greatDecr = "{:.0f}".format(greatDecr)
    greatIncr = "{:.0f}".format(greatIncr)
    
    #print to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {totalMonths}')
    print(f'Total: ${totalMoney}')
    print(f'Average Change: ${averageProfLoss}')
    print(f'Greatest Increase in Profits: {greatIncrMonth} (${greatIncr})')
    print(f'Greatest Decrease in Profits: {greatDecrMonth} (${greatDecr})')

#print to txt file
output_path = os.path.join("..", "PyBank", "financial_analysis.txt")
with open(output_path, 'w', newline='') as financialAnalysisFile:
    financialAnalysisFile.write("Financial Analysis\n")
    financialAnalysisFile.write("----------------------------\n")
    financialAnalysisFile.write(f'Total Months: {totalMonths}\n')
    financialAnalysisFile.write(f'Total: ${totalMoney}\n')
    financialAnalysisFile.write(f'Average Change: ${averageProfLoss}\n')
    financialAnalysisFile.write(f'Greatest Increase in Profits: {greatIncrMonth} (${greatIncr})\n')
    financialAnalysisFile.write(f'Greatest Decrease in Profits: {greatDecrMonth} (${greatDecr})\n')














        

 