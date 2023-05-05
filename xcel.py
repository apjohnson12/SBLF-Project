import os
import math
from openpyxl import Workbook

directory_path = os.path.join(os.path.dirname(__file__), 'CoverageData')  # directory path relative to script location
output_file_path = os.path.join(os.path.dirname(__file__), 'data1.xlsx')  # output file path relative to script location
total_lines = 0
total_files = 0
lines_dict = {}
total_pass = 0
total_fail = 0
skip_first_line = True

# first pass to read through all files and calculate counts
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f):
                line = line.strip()  # remove whitespace from beginning and end of line
                if skip_first_line:
                    skip_first_line = False
                    first_line = line.split(' ', 1)
                    is_true = True if first_line[1] == 'true' else False
                    continue  # skip the first line
                if line not in lines_dict:
                    # if line is not already in lines_dict, add it with counts of 1 and 0
                    lines_dict[line] = {'true': int(is_true), 'false': int(not is_true), 'total': 1}
                else:
                    # if line is already in lines_dict, increment its counts
                    lines_dict[line]['true'] += int(is_true)
                    lines_dict[line]['false'] += int(not is_true)
                    lines_dict[line]['total'] += 1
                total_lines += 1
                if is_true:
                    total_pass += 1
                else:
                    total_fail += 1
        total_files += 1
        skip_first_line = True  # reset flag for next file

# create Excel workbook and sheet
wb = Workbook()
ws = wb.active

# add headers to Excel sheet
ws.append(['Line', 'Total', 'Tarantula', 'Jaccard', 'SBI', 'Ochiai', 'Pass', 'Fail'])

# loop through lines_dict and write results to Excel sheet
for line, counts in lines_dict.items():
    true_count = counts['true']
    false_count = counts['false']
    total_count = counts['total']
    tarantula = tarantula = (false_count / total_fail) / ((false_count / total_fail) + (true_count / total_pass))
    jaccard = false_count / (total_fail + true_count)
    sbi = false_count / (false_count + true_count)
    ochiai = false_count / math.sqrt(total_fail * (true_count + false_count))
    ws.append([line, total_count, tarantula, jaccard, sbi, ochiai, true_count, false_count])

# save the Excel workbook
wb.save(output_file_path)