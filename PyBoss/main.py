import os
import csv
from datetime import datetime

input_file = 'employee_data1.csv'
output_file = 'employee_data1_cleaned.csv'

# state abbreviation library
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# declare lists
emp_id, full_name, first_name, last_name, dob, dob_modified, ssn, ssn_filtered, state, state_abbrev = ([] for i in range(10))

# input path and output paths
csv_path = os.path.join('raw_data', input_file)
cleaned_csv_path = os.path.join('clean_data', output_file)


# pull data from unformatted csv files and load lists
with open(csv_path, mode='r', newline='') as employee_data:
    reader = csv.reader(employee_data)

    # skip headers before loading lists
    next(reader)

    # gather original data for modification and load into lists
    for row in reader:
        emp_id.append(row[0])
        full_name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])


# modify lists to new format
for i in range(len(full_name)):

    # name modification
    split_name = full_name[i].split(" ")
    first_name.append(split_name[0])
    last_name.append(split_name[1])

    # dob modification
    date_strip = datetime.strptime(dob[i], '%Y-%m-%d').strftime('%m/%d/%Y')
    dob_modified.append(date_strip)

    # ssn modification
    ssn_obscured = "***-**-" + ssn[i][-4:]
    ssn_filtered.append(ssn_obscured)

    # state abbreviation modification
    state_two_letter = us_state_abbrev[state[i]]
    state_abbrev.append(state_two_letter)


# *------------------------*
# |  Output Modifications  |
# *------------------------*

# zip modified values then output it into a new csv
cleaned_data_header = [('Employee_ID', 'First_Name', 'Last_Name', 'DOB', 'SSN', 'State')]
cleaned_data_values = zip(emp_id, first_name, last_name, dob_modified, ssn_filtered, state_abbrev)


with open(cleaned_csv_path, mode='w', newline='') as modified_data:
    writer = csv.writer(modified_data)

    writer.writerows(cleaned_data_header)
    writer.writerows(cleaned_data_values)
