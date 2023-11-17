import csv


def financial_analysis(csv_file_path):
    # Initialize variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    changes = []
    dates = []

    # Open the CSV file
    with open(csv_file_path, 'r') as file:
        # Create a CSV reader
        csv_reader = csv.reader(file)

        # Skip the header row
        header = next(csv_reader)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Extract date and profit/loss values
            date = row[0]
            profit_loss = int(row[1])

            # Calculate the total number of months
            total_months += 1

            # Calculate the net total amount of profit/losses
            net_total += profit_loss

            # Calculate the change in profit/loss
            if total_months > 1:
                change = profit_loss - previous_profit_loss
                changes.append(change)
                dates.append(date)

            # Update the previous profit/loss for the next iteration
            previous_profit_loss = profit_loss

    # Calculate the average change
    average_change = sum(changes) / len(changes)

    # Find the greatest increase and decrease in profits
    greatest_increase = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase)]
    greatest_decrease = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease)]

    # Print the results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total: ${net_total}")
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Replace "budget_data.csv" with the actual path to your CSV file
csv_file_path = "Resources/budget_data.csv"
financial_analysis(csv_file_path)
