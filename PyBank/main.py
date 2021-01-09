#PyBank

import os
import csv

#Path to collect data: PyBank/Resources/budget_data.csv
budget_csv = os.path.join('Resources', 'budget_data.csv')
   
with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # Calculate total number of months included in the dataset
    # Counting the first row after the header to determine where the calculations start
    first_row = next(csvreader)
    
    # Starting total months at 1 since this is set to start on the first row    
    total_months = 1
 
    prev_pl = int(first_row[1])
    total_pl = prev_pl

    max_pl_change = 0
    min_pl_change = 0
    total_pl_change = 0
   
    # Read each row of data after the header
    for row in csvreader:
        total_months +=1           
        total_pl += int(row[1])
        pl_change = int(row[1])-prev_pl
        prev_pl = int(row[1])
        total_pl_change += pl_change

        if pl_change > max_pl_change:
            max_pl_change = pl_change
            max_pl_change_date = str(row[0])


        if pl_change < min_pl_change:
            min_pl_change = pl_change
            min_pl_change_date = str(row[0])
        
    # Reduce the # of months for the denominator because 1 fewer month of change
    average_change = total_pl_change/(total_months-1)
	

# Print the analysis to the terminal and export a text file with the results

analysis_file = os.path.join('analysis','analysis_file.txt')
with open (analysis_file, "w", newline = "") as outfile:
    print("Financial Analysis", file = outfile)
    print ("-----------------------------------", file = outfile)
    print (f"Total Months: {total_months}", file = outfile)
    print (f"Total: ${total_pl}", file = outfile)
    print (f"Average Change: $({average_change: .2f})", file = outfile)
    	# adding in : .2f ensures that it only returns 2 decimal places
    print (f"Greatest Increase in Profits: {max_pl_change_date} (${max_pl_change})", file = outfile)
    print (f"Greatest Decrease in Profits: {min_pl_change_date} (${min_pl_change})", file = outfile)
    
with open(analysis_file, "r", newline = "") as outfile:

    print (outfile.read())



