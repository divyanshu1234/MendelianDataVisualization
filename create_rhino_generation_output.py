from tkinter.filedialog import askopenfilename
import pandas as pd


def create_file(dataframe, a, b, c, mult_a, mult_b, mult_c, name):
    output_dict = {
        'a': dataframe[a] * mult_a,
        'b': dataframe[b] * mult_b,
        'c': dataframe[c] * mult_c
    }

    pd.DataFrame(output_dict).to_csv("Outputs/" + name + ".csv", index=False, header=False)


input_filename = askopenfilename()
input_dataframe = pd.read_csv(input_filename)


# Org 1
create_file(input_dataframe, 'time', 'org1_x', 'org1_x', 0.01, 1, 0, 'org1_x')  # X
create_file(input_dataframe, 'org1_y', 'time', 'org1_y', 0, 0.01, 1, 'org1_y')  # Y
create_file(input_dataframe, 'org1_z', 'org1_z', 'time', 0, 1, 0.01, 'org1_z')  # Z

# Org 2
create_file(input_dataframe, 'time', 'org2_x', 'org2_x', 0.01, 1, 0, 'org2_x')  # X
create_file(input_dataframe, 'org2_y', 'time', 'org2_y', 0, 0.01, 1, 'org2_y')  # Y
create_file(input_dataframe, 'org2_z', 'org1_z', 'time', 0, 1, 0.01, 'org2_z')  # Z
