import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 get_features.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage1", "train.csv")
os.makedirs(os.path.join("data", "stage1"), exist_ok=True)

def process_data(fd_in, fd_out):
    fd_in.readline()
    for line in fd_in:
        line = line.rstrip('\n').split(',')

        age = line[0]
        sex = line[1]
        income = line[2]
        degree = line[3]
        marital_status = line[4]
        num_of_children = line[5]
        home_ownership = line[6]
        credit_score = line[7]
        
        fd_out.write("{},{},{},{},{},{},{},{}\n".format(age, 
                                                        sex,
                                                        income, 
                                                        degree, 
                                                        marital_status, 
                                                        num_of_children, 
                                                        home_ownership, 
                                                        credit_score))


with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
