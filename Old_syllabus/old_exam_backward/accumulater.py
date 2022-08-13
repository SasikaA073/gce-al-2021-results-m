import os,csv

python_file_path = __file__
python_file_path = python_file_path.split("\\")
folder_path = '\\'.join(python_file_path[:-1]) + '\\'

print(folder_path)
final_path = folder_path + "final"

start = 1102200

end = -184200

# start = 1102200
# end = start - 400
lap = 200
num = 2

with open(f"{final_path}\\final{num}.csv",'w',newline="") as final_file:
    # csvwriter = csv.writer(final_file)
    for i in range(end,start+lap,lap):
        with open(f"results_{i}.csv",'r') as input_file:
            content = input_file.readlines()
            # print(content)
            # csvwriter.writer(content)
            # final_file.writelines(content)
            # print(i,"done")
            for j in range(len(content)-1,-1,-1):
                line = content[j]
                print(line)
                final_file.writelines(line)
            print(i,"done")