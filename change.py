# import os
# import random

# directory_path = './CoverageData'  # directory path
# files_list = os.listdir(directory_path)
# num_files = len(files_list)
# num_files_to_modify = int(num_files * 0.1)  # modify 10% of the files

# files_to_modify = random.sample(files_list, num_files_to_modify)  # randomly select files to modify

# for filename in files_to_modify:
#     file_path = os.path.join(directory_path, filename)
#     with open(file_path, 'r') as f:
#         lines = f.readlines()
#     lines[0] = lines[0].replace('true', 'false', 1)  # replace first occurrence of 'true' with 'false'
#     with open(file_path, 'w') as f:
#         f.writelines(lines)



import os

directory_path = './CoverageData'  # directory path relative to script location
output_file_path = './var.txt'  # output file path relative to script location

with open(output_file_path, 'w') as output_file:
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                first_line = f.readline().strip()
                output_file.write(f'{filename}: {first_line}\n')
