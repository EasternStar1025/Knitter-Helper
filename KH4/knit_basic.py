# Basic coding for knitter function

project_name = []
project_type = []
project_yarn = []
project_needle = []
data = [project_name, project_type, project_yarn, project_needle]
full_list = tuple(data)
file = "Test_Knit.txt"
try:
    open(file, 'x')
    print("File Created")
except:
    print("File Opened")

project_name_entry = input("Enter in a project name: ")
project_name.append(project_name_entry)

project_type_entry = input("Enter in the type of project: ")
project_type.append(project_type_entry)

project_yarn_entry = input("Enter in the yarn needed: ")
project_yarn.append(project_yarn_entry)

project_needle_entry = input("Enter in the needles used: ")
project_needle.append(project_needle_entry)

data.append(full_list)

file_path = "Test_Knit.txt"

with open(file, 'a') as file:
    file.write(str(data) + '\n')
with open(file_path, "r") as file:
    print(file.read())
    file.close()
    