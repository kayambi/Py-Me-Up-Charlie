#import os
# Module for reading CSV files
import csv
months_list = []
total_net_amount_list = []
least_month = ''

#csvpath = os.path.join("." ,"Resources",'02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
csvpath = "/Users/musafirikayambi/Desktop/budget_data.csv"
#output_file = open(output_file_str, "w")


with open(csvpath, newline='',) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    
    csvreader = csv.reader(csvfile,delimiter =',')
    print("csvreader")
    header =next(csvreader)
    print(f"CSV Header: {header}")
    
    for row in csvreader:
        #print(row)
        months_list.append(row[0])
        total_net_amount_list.append(int(row[1]))
    print("Total Months", len(months_list))
    print("Total Net Amount", sum(total_net_amount_list)) 

    #average change

    first = int(total_net_amount_list[0])
    last = int(total_net_amount_list[len(months_list) - 1])
    average_change = ((last - first)/(len(months_list) -1 ))
    print(f'Average change: $ {round(average_change,2)}')

    # greatest increase 
    
    least_value = 0 
    greatest_value = 0
    for i in range(len(total_net_amount_list) - 1):
        num = int(total_net_amount_list[i])
        num_next = int(total_net_amount_list[i + 1])
        value = num_next - num
        if(value > greatest_value):
            greatest_value = value
            greatest_month = months_list[i + 1]

        if(value < least_value):
            least_value = value
            least_month = months_list[i + 1]
    print(f"Greatest Increase In Profits: {greatest_month} (${greatest_value})")
    print(f"Greatest Decrease In Profits: {least_month} (${least_value})")
