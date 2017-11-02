from tkinter.filedialog import askopenfilename
import pandas as pd


input_filename = askopenfilename()
input_dataframe = pd.read_csv(input_filename)


# X
a = input_dataframe['time'] / 100
b = input_dataframe['h']
c = input_dataframe['h'] * 0

x_dict = {
    'a': a,
    'b': b,
    'c': c
}
pd.DataFrame(x_dict).to_csv('Outputs/x.csv', index=False, header=False)


# Y
a = input_dataframe['s'] * 0
b = input_dataframe['time'] / 100
c = input_dataframe['s'] * 360

y_dict = {
    'a': a,
    'b': b,
    'c': c
}
pd.DataFrame(y_dict).to_csv('Outputs/y.csv', index=False, header=False)


# Z
a = input_dataframe['v'] * 0
b = input_dataframe['v'] * 360
c = input_dataframe['time'] / 100

z_dict = {
    'a': a,
    'b': b,
    'c': c
}
pd.DataFrame(z_dict).to_csv('Outputs/z.csv', index=False, header=False)
