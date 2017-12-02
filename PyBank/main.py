import os
import csv

Date, Revenue = ([] for i in range(2))

# input and output files
input_file = "budget_data_1.csv"
output_file = "budget_data_1_summary.txt"

# input and output paths
csv_input_path = os.path.join("raw_data", input_file)
txt_output_path = os.path.join("summary_doc", output_file)


with open(csv_input_path, mode='r', newline='') as budget_data:
    reader = csv.reader(budget_data, delimiter=',')

    next(reader)

    row_num = 0
    for row in reader:
        Date.append(row[0])
        Revenue.append(row[1])
        row_num += 1
        
# print summary header
print("\nFinancial Analysis", "\n" + "-" * 50)


# sum of months
print("Total Months:", row_num)

# sum of revenue
revenue_sum = 0
for i in Revenue:
    revenue_sum += int(i)

print("Total Revenue: $" + str(revenue_sum))



# average revenue change
total_revenue_change = 0
for h in range(row_num):
    total_revenue_change += int(Revenue[h]) - int(Revenue[h - 1])
    
    
print(total_revenue_change)


# the first_pass variable is created to remove the first iteration revenue change
# which, takes the first list element and subtracts it by the last list element.
first_pass = (int(Revenue[0]) - int(Revenue[-1]))
total_revenue_change_adj = total_revenue_change - first_pass



avg_revenue_change = (total_revenue_change_adj + int(Revenue[0])) / row_num
print("Average Revenue Change: $" + str(round(avg_revenue_change)))



# greatest increase in revenue
high_revenue = 0
for j in range(len(Revenue)):
    if int(Revenue[j]) - int(Revenue[j - 1]) > high_revenue:
        high_revenue = int(Revenue[j]) - int(Revenue[j - 1])
        high_month = date[j]

print("Greatest Increase in Revenue:", high_month, "($" + str(high_revenue) + ")")



# greatest decrease in revenue
low_revenue = 0
for k in range(len(Revenue)):
    if int(Revenue[k]) - int(Revenue[k - 1]) < low_revenue:
        low_revenue = int(Revenue[k]) - int(Revenue[k - 1])
        low_month = date[k]

print("Greatest Decrease in Revenue:", low_month, "($" + str(low_revenue) + ")")


with open(txt_output_path, mode='w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)

    writer.writerows([
        ["Financial Analysis for: " + input_file],
        ["-" * 50],
        ["Total Months: " + str(row_num)],
        ["Total Revenue: $" + str(revenue_sum)],
        ["Average Revenue Change: $" + str(round(avg_revenue_change))],
        ["Greatest Increase in Revenue: " + str(high_month) + " ($" + str(high_revenue) + ")"],
        ["Greatest Decrease in Revenue: " + str(low_month) + " ($" + str(low_revenue) + ")"]
    ])

