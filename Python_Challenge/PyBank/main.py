# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_profit_loss = None
net_change_list = []
greatest_increase = ("", 0)  # (date, amount)
greatest_decrease = ("", 0)  # (date, amount)

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Track the total months and net total
        total_months += 1
        total_net += profit_loss
        
        # Track the net change
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            net_change_list.append(change)

            # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase[1]:
                greatest_increase = (date, change)

            # Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease[1]:
                greatest_decrease = (date, change)

        previous_profit_loss = profit_loss

# Calculate the average net change across the months
if net_change_list:
    average_change = sum(net_change_list) / len(net_change_list)
else:
    average_change = 0

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total Profit/Losses: ${total_net}\n"
    f"Average Change in Profit/Losses: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
