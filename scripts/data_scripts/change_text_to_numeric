import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 change_text_to_numeric.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage3", "train.csv")
os.makedirs(os.path.join("data", "stage3"), exist_ok=True)


def encode_degree(degree_str):

    if degree_str == "High School Diploma":
        degree_num = 0
    elif degree_str == "Associate's Degree":
        degree_num = 1
    elif degree_str == "Bachelor's Degree":
        degree_num = 2
    elif degree_str == "Master's Degree":
        degree_num = 3
    elif degree_str == "Doctorate":
        degree_num = 4

    return degree_num


def encode_sex(sex_str):

    if sex_str == 'Male':
        sex_num = 0
    else:
        sex_num = 1

    return sex_num


def encode_sex(marital_status_str):

    if marital_status_str == 'Single':
        marital_status_num = 0
    else:
        marital_status_num = 1

    return marital_status_num


def encode_marital_status(marital_status_str):

    if marital_status_str == 'Single':
        marital_status_num = 0
    else:
        marital_status_num = 1

    return marital_status_num


def encode_home_ownership(home_ownership_str):

    if home_ownership_str == 'Rented':
        home_ownership_num = 0
    else:
        home_ownership_num = 1

    return home_ownership_num


def encode_credit_score(credit_score_str):

    if credit_score_str == 'Low':
        credit_score_num = 0
    elif credit_score_str == 'Average':
        credit_score_num = 1
    else:
        credit_score_num = 2

    return credit_score_num


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
        
        arr_age.append(line[0])
        arr_sex.append(line[1])
        arr_income.append(line[2])
        arr_degree.append(line[3])
        arr_marital_status.append(line[4])
        arr_num_of_children.append(line[5])
        arr_home_ownership.append(line[6])
        arr_credit_score.append(line[7])

    for i in range(len(arr_age)):
        arr_sex[i] = encode_sex(arr_sex[i])
        arr_degree[i] = encode_degree(arr_degree[i])
        arr_marital_status[i] = encode_marital_status(arr_marital_status[i])
        arr_home_ownership[i] = encode_home_ownership(arr_home_ownership[i])
        arr_credit_score[i] = encode_credit_score(arr_credit_score[i])


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
