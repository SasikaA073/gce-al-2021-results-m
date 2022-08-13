import os,csv

python_file_path = __file__
python_file_path = python_file_path.split("\\")
folder_path = '\\'.join(python_file_path[:-1]) + '\\'

print(folder_path)
final_path = folder_path + "final"

start = 1102200
# end = start + 400
end =   4150600
lap = 200
num = 1

with open(f"{final_path}\\final{num}.csv",'w',newline="") as final_file:
    # csvwriter = csv.writer(final_file)
    for i in range(start,end+lap,lap):
        with open(f"results_{i}.csv",'r') as input_file:
            content = input_file.readlines()
            # print(content)
            # csvwriter.writer(content)
            final_file.writelines(content)
            print(i,"done")