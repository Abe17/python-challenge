#ANALYSIS:
#The total number of months included in the dataset
#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profizt/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import csv

# Definition of variables
month_count = 0
total_profit = 0
pl_current_month = 0
pl_previous = 0
change_mtm_sum = []
test = []

# Output csv file:
budget_data = r"C:\Users\vb_ab\pythonfiles\homework\python_challenge\budget_data.csv"

dates_for_change = {}

with open(budget_data) as csvfile:
  
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        
        date = row[0]
        month_count += 1
        profit_losses = row[1]
        total_profit = total_profit + int(profit_losses)

        change = int(profit_losses)- int(pl_previous)
        change_mtm_sum.append(int(profit_losses) - int(pl_previous))
     
        pl_previous = row[1]
        dates_for_change[change] = date

print(dates_for_change)

# print max and min values
max(change_mtm_sum)
change_mtm_sum.pop(0)
avg_mtm = sum(change_mtm_sum) / (month_count-1)
greatest_increase_change = max(change_mtm_sum)
greatest_decrease_change = min(change_mtm_sum)

greatest_month_increase = dates_for_change[greatest_increase_change]
greatest_month_decrease = dates_for_change[greatest_decrease_change]

print("Financial Analysis")
print("----------------------------")
print("Total Months:" + " " + str(month_count))
print("Total:" + " " + "$" + str(total_profit))
print(f"Average Change: $ {avg_mtm:.2f}")
print("Greatest Increase in Profits:" + " " + greatest_month_increase + " " + "($" + str(greatest_increase_change) + ")")

# print changes
print("Greatest Decrease in Profits:" + " " + greatest_month_decrease + " " + "($" + str(greatest_decrease_change) + ")")
index_month_increase = change_mtm_sum.index(max(change_mtm_sum))
index_month_decrease = change_mtm_sum.index(min(change_mtm_sum))


