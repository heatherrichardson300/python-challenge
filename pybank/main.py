import csv
import os

file_path = os.path.join('Resources', 'budget_data.csv')
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

#intialize counters and create variables to hold information 
total_months = 0
total_net = 0
greatest_increase = -float('inf')
greatest_decrease = float('inf')
previous_change = 0
month_decrease = ''
month_increase = ''
monthly_changes = []

#open file
with open(file_path, 'r') as financial_data:
    reader = csv.reader(financial_data, delimiter= ',')    

    next(reader) #skip header
    
    for row in reader: #loop through the rows

        #using the total_month counter to count the rows
        total_months += 1
      
        #totaling the profit/losses in row[1]
        total_net += int(row[1])

        #tracking the month to month changes by storing in a variable 
        monthly_change = int(row[1]) - previous_change
        previous_change = int(row[1])
        monthly_changes.append(monthly_change)

        #tracking the greatest increase in profits
        if monthly_change > greatest_increase:
            greatest_increase = monthly_change
            month_increase = row[0]
        #tracking the greates decrease in profits
        elif monthly_change < greatest_decrease:
            month_decrease = row[0]
            greatest_decrease = monthly_change 
        #capture the average
        average = (sum(monthly_changes) - monthly_changes[0]) / 85

#place calculations into a variable with f string statements
summary_data = (
    f'Total months: {total_months} months\n'
    f'Total net: ${total_net}\n'
    f'Average Profit Change: ${round(average, 2)}\n' #round the percentage
    f"Greatest Increase in Profits: {month_increase} ${greatest_increase}\n"
    f"Greatest Decrease in Profits: {month_decrease} ${greatest_decrease}\n"
)
#print calculations to terminal 
print(summary_data)

with open(file_to_output, 'w') as newfile:
    newfile.write('Summary Data\n') #create header
    newfile.write(summary_data) #write calculations
