import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 fill_na.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage2", "train.csv")
os.makedirs(os.path.join("data", "stage2"), exist_ok=True)

def process_data(fd_in, fd_out):
    arr_age = []
    arr_sex = []
    arr_income = []
    arr_degree = []
    arr_marital_status = []
    arr_num_of_children = []
    arr_home_ownership = []
    arr_credit_score = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')

        arr_sex.append(line[1])
        arr_income.append(line[2])
        arr_degree.append(line[3])
        arr_marital_status.append(line[4])
        arr_num_of_children.append(line[5])
        arr_home_ownership.append(line[6])
        arr_credit_score.append(line[7])

        if line[0]:
            arr_age.append(int(line[0]))
        else:
            arr_age.append(0)

    s = sum(arr_age)

    for i in range(len(arr_age)):
        if arr_age[i] == 0:
            arr_age[i] = round(s / len(arr_age), 0)

    for age, sex, income, degree, marital_status, num_of_children, home_ownership, credit_score in zip(arr_age,
                                                                                                       arr_sex,
                                                                                                       arr_income,
                                                                                                       arr_degree,
                                                                                                       arr_marital_status,
                                                                                                       arr_num_of_children,
                                                                                                       arr_home_ownership,
                                                                                                       arr_credit_score):
        
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
