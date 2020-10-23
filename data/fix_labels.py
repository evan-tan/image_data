import os
import pathlib as pl
import sys


if __name__ == "__main__":
    cur_dir = os.getcwd()
    fix_dir = cur_dir + "/fix"
    all_lines = []
    for file_name in os.listdir(fix_dir):
        if file_name.endswith(".txt"):
            with open(fix_dir + "/" + file_name, "r") as f_obj:
                for line in f_obj.readlines():
                    line = line.strip()
                    line = line.split(" ")
                    new_line = [str(item) for item in line]
                    print(new_line)
                    new_line[0] = "0"
                    nl = new_line
                    new_line = nl[0] + " " + nl[1] + " " + nl[2] + " " + nl[3] + " " + nl[4]
                    # print(new_line)
                    # with open(fix_dir + "/" + file_name, "w") as fout:
                    #     fout.write(new_line)
