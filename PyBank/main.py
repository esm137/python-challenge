import os
import csv
import sys

TotalMonths=0
TotalProfit=0
AverageChange=0
GreatestIncrease=0
GreatestIncreaseMonth=""
GreatestDecrease=0
GreatestDecreaseMonth=""
TotalChange=0
PreviousProfit=0


CsvPath= os.path.join("Resources","budget_data.csv")

with open(CsvPath) as CsvFile:
    CsvReader= csv.reader(CsvFile, delimiter=",")


    for i in CsvReader:
        if TotalMonths>0:
            if TotalMonths>1:
                TotalChange+=(float(i[1])-PreviousProfit)
                if (float(i[1])-PreviousProfit)>GreatestIncrease:
                    GreatestIncrease=float(i[1])-PreviousProfit
                    GreatestIncreaseMonth=i[0]
                if (float(i[1])-PreviousProfit)<GreatestDecrease:
                    GreatestDecrease=float(i[1])-PreviousProfit
                    GreatestDecreaseMonth=i[0]
            TotalProfit+=float(i[1])
            PreviousProfit=float(i[1])
        TotalMonths+=1
        
    
    AverageChange=TotalChange/(TotalMonths-2)
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {TotalMonths-1}")
    print(f"Average Change: ${round(AverageChange,2)}")
    print(f"Greatest Increase in Profit: {GreatestIncreaseMonth} (${GreatestIncrease})")
    print(f"Greatest Decrease in Profit: {GreatestDecreaseMonth} (${GreatestDecrease})")
with open("Analysis/Analysis.txt","w") as f:
    sys.stdout=f
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {TotalMonths-1}")
    print(f"Average Change: ${round(AverageChange,2)}")
    print(f"Greatest Increase in Profit: {GreatestIncreaseMonth} (${GreatestIncrease})")
    print(f"Greatest Decrease in Profit: {GreatestDecreaseMonth} (${GreatestDecrease})")