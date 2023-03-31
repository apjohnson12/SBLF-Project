import sys #unused import
import os

path = os.path.join(os.getcwd(), "CoverageData") #platform indedepent file path

os.chdir(path)

class Method:
    def __init__(self, name, passed, failed, total):
        self.name = name
        self.passed = passed
        self.failed = failed
        self.total = total

method_list = []

def read_text_file(file_path, method_list):
    with open(file_path, 'r') as f:
        Lines = f.readlines()
        test_result = ''
        for index, line in enumerate(Lines):
            method = Method('', 0, 0, 0)
            if index == 0:
                parse = Lines[0].split()
                test_result = parse[1]
            else:
                method.name = line

                #check to see if that source code method exists in our method list
                for m in method_list:
                    if m.name == method.name:
                        if test_result == "true":
                            m.passed += 1
                            m.total += 1
                            return
                        else:
                            m.failed += 1
                            m.total += 1
                            return

                #if no method object exists for that method    
                method.total = 1
                if test_result == "true":
                    method.passed = 1
                    method.failed = 0
                    # print(method.passed)
                    method_list.append(method)
                else:
                    method.passed = 0
                    method.failed = 1
                    # print(method.passed)
                    method_list.append(method) 

           


for file in os.listdir():
    file_path=os.path.join(path, file) #platform independent file path
    read_text_file(file_path, method_list)
    # print("\n")
    
for m in method_list:
    print(m.total, m.name)
