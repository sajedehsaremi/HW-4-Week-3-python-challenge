# Import Dependencies
import os
import csv
import sys

# Set Path for files
CSVpath = os.path.join("PyBank/Resources", "budget_data.csv")

# Output files
output_file = os.path.join("python-challenge", "PyBank", "Analysis_Summary.txt")


# Create the empty lists for the following variables
monthly_profit_change = []
 
# Open csv file
with open("C:/Users/Sajedeh/personal-class/gt-atl-data-pt-06-2021-u-c/03-Python/02-Homework/Instructions/PyBank/Resources/budget_data.csv",newline="", encoding="utf-8") as budget:

     # Creat the contents of budget_data.csv in the variable csvreader
    Budget = csv.reader(budget,delimiter=",") 

# Creat list based on CSV columns
    file = csv.DictReader(budget)
    month = []
    profit = []
    for col in file:
        month.append(col["Date"])
        profit.append(col["Profit/Losses"])


    print("Total number of months:", len(month))

# convert text to integer for column profit
    for i in range(0, len(profit)):
       profit[i] = int(profit[i])
    print("Net total amount of Profit/Losses:", sum(profit))
    print("Average of the changes in Profit/Losses:", sum(profit)/len(profit))
    print("Greatest increase in Profit/Losses:", max(profit))
    print("Greatest decrease in Profit/Losses:", min(profit))
    
# Write the output in the text file
    with open("C:/Users/Sajedeh/personal-class/HW-4-Week-3-python-challenge/HW-4-Week-3-python-challenge/PyBank/Analysis/PyBank_result.txt", 'w') as f:
        print("Total number of months:", len(month), file=f)
        print("-------------------------------", file=f)
        for i in range(0, len(profit)):
            profit[i] = int(profit[i])
        print("Net total amount of Profit/Losses:", sum(profit),file=f)
        print("Average of the changes in Profit/Losses:", sum(profit)/len(profit),file=f)
        print("Greatest increase in Profit/Losses:", max(profit),file=f)
        print("Greatest decrease in Profit/Losses:", min(profit),file=f)
