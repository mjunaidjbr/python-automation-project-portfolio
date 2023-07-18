import os
import subprocess

#intall the dependencies if not already installed
try:
    import openpyxl
except ImportError:
    subprocess.call(["pip", "install", "openpyxl"])
    import openpyxl

try:
    import pandas as pd
except ImportError:
    subprocess.call(["pip", "install", "pandas"])
    import pandas as pd




#input file name
# input_file_name = "leads.xlsx"
#ask from user 
input_file_name = str(input("Enter the file name: "))
#check file exists 
#script path using os

script_path = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists(input_file_name):
    print(f"{input_file_name} not found in the script directory {str(os.path.dirname(os.path.realpath(__file__)))}")
    exit()

#output file name
output_file_name = input_file_name.replace(".xlsx", ".csv")

#remove output_file_name if exists
if os.path.exists(output_file_name):
    os.remove(output_file_name)


#convert xlsx file to csv format
df = pd.read_excel(input_file_name)
df.to_csv("temp1.csv",header=False,index=False)

# #replace the delimeter "#" with ","
# with open("temp1.csv", "r",encoding="utf8") as file:
#     for line in file:
#         # print(line.replace("#", ","))
#         #save the line to a file leads1.csv
#         with open("temp2.csv", "a",encoding="utf8") as f:
#             f.write(line.replace("#", ","))
#             # f.write("\n")
#             f.close()

#remove the dublicate lines
with open("temp1.csv", "r",encoding="utf8") as f:
    perv=""
    for line in f:
        split1 = line.split('#')
        split2 = perv.split('#')
        if ','.join(split1[1::]) != ','.join(split2[1::]):
            #save line to file output_file_name
            with open(output_file_name, "a",encoding="utf8") as f:
                f.write(line)
        perv=line

#remove the temporary files
if os.path.exists("temp1.csv"):
    os.remove("temp1.csv")

# if os.path.exists("temp2.csv"):
#     os.remove("temp2.csv")


print(f"output file: %s" % output_file_name)
print(f"please check the output file in the script folder {str(os.path.dirname(os.path.realpath(__file__)))}")