import os

directory_path = os.path.join(os.path.dirname(__file__), 'CoverageData')  # directory path relative to script location
output_file_path = os.path.join(os.path.dirname(__file__), 'data.txt')  # output file path relative to script location
total_lines = 0
total_files = 0
lines_dict = {}
skip_first_line = True

for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()  # remove whitespace from beginning and end of line
                if skip_first_line:
                    # parse first line for true/false value
                    skip_first_line = False
                    _, value = line.split(' ', 1)
                    continue  # skip the first line
                if line not in lines_dict:
                    # if line is not already in lines_dict, add it with a count of 1 and true/false counts
                    lines_dict[line] = {'count': 1, 'true': 0, 'false': 0}
                else:
                    # if line is already in lines_dict, increment its count and true/false counts
                    lines_dict[line]['count'] += 1
                if value.lower() == 'true':
                    lines_dict[line]['true'] += 1
                elif value.lower() == 'false':
                    lines_dict[line]['false'] += 1
                total_lines += 1
        total_files += 1
        skip_first_line = True  # reset flag for next file

with open(output_file_path, 'w') as output_file:
    output_file.write(f'Total lines: {total_lines}\n')
    output_file.write(f'Total files: {total_files}\n')
    output_file.write(f'Unique lines: {len(lines_dict)}\n')
    output_file.write('---\n')
    for line, counts in lines_dict.items():
        output_file.write(f"{line} ({counts['count']} times, {counts['true']} true, {counts['false']} false)\n")

