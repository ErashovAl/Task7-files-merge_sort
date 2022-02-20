import os
from operator import itemgetter

def main(path):
    # BASE = os.getcwd()
    file_list = []

    for file in os.listdir(path):
        if file.endswith('.txt'):
            with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                read = f.read().strip()
                num_string = int(read.count('\n') + 1)
                file_list.append([str(num_string), file, read])
      
    sorted_list = sorted(file_list, key=itemgetter(0))
    
    with open(os.path.join("solution.txt"), "w", encoding='utf-8') as f:
        for file in sorted_list:
            # line_break = "\n"
            # line_break_num = 2
            
            # if sorted_list.index(file) == len(sorted_list)-1:
                # line_break_num = 0
            total = f"имя: {file[1]}\nкол-во строк: {file[0]}\n{file[2].strip()}\n\n"
            f.write(total)

main("./files")