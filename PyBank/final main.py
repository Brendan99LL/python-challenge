import os
import csv
from pathlib import Path

PyBank_csv = os.path.join(".", "Resources", "budget_data.csv")

# Make empty lists to distiguish between rows
months = []
profits = []
profit_change = []
profit = 0

# Open and read csv
with open (PyBank_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)

    # Loop through the lists made 
    for row in csv_reader:

        # Make sure the values given to the variables for the lists are actually placed in the lists for future use
        # Append moves the values into the lists
        months.append(row[0])
        total_months = len(months)
        
        #profits = profits + int(row[1])
        profits.append(int(row[1]))
        total_profits = sum(profits)
    
    # Loop through the profit list to start calculating the change
    for i in range(len(profits) - 1):

        # Append the change values into the developed list for the changes
        profit_change.append(profits[i + 1] - profits[i])

        # Calculate the average with the changes
        average = sum(profit_change) / len(profit_change)
        average_change = "{:.2f}".format(average)

# Grab the max profits and changes from the profit and change lists
greatest_increase_profit = max(profit_change)

greatest_increase_month = profit_change.index(max(profit_change)) + 1


# Grab the min profits and changes from the profit and change lists
greatest_decrease_profit = max(profit_change)

greatest_decrease_month = profit_change.index(min(profit_change)) + 1




# Print the final variables based on the image
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {months[greatest_increase_month]} (${(str(greatest_increase_profit))})")
print(f"Greatest Decrease in Profits: {months[greatest_decrease_month]} (${(str(greatest_decrease_profit))})")


# Print the final variables onto another exported text file
# Name the path a differentname then what the excel file is
PyBank_text = os.path.join(".", "Analysis", "PyBank_Text_Results.txt")
with open(PyBank_text, "w") as text_file:
    print("Financial Analysis", file = text_file)
    print("-------------------------------", file = text_file)
    print(f"Total Months: {total_months}", file = text_file)
    print(f"Total: ${total_profits}", file = text_file)
    print(f"Average Change: ${average_change}", file = text_file)
    print(f"Greatest Increase in Profits: {months[greatest_increase_month]} (${(str(greatest_increase_profit))})", file = text_file)
    print(f"Greatest Decrease in Profits: {months[greatest_decrease_month]} (${(str(greatest_decrease_profit))})", file = text_file)




