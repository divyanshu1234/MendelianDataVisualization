from tkinter.filedialog import askopenfilename

import Helpers.helper as helper
import pandas as pd

from Helpers import organism

input_filename = askopenfilename()
input_dataframe = pd.read_csv(input_filename)


helper.trans_data['A'] = input_dataframe[['acc_x', 'acc_y', 'acc_z']].as_matrix() * 10
helper.trans_data['R'] = input_dataframe[['rot_x', 'rot_y', 'rot_z']].as_matrix()
helper.trans_data['I'] = input_dataframe['light_intensity'] / input_dataframe['light_intensity'].max()
time = input_dataframe['time']

xyz_gen0 = input_dataframe[['h', 's', 'v']].as_matrix()
xyz_gen0[:, 1] = xyz_gen0[:, 1] * 360
xyz_gen0[:, 2] = xyz_gen0[:, 2] * 360

genome_gen0_org1 = input("Genome org1 (AaRrIi): ")
genome_gen0_org2 = input("Genome org2 (AaRrIi): ")
max_gen = int(input("Max Generation: "))

org1 = organism.Organism(xyz=xyz_gen0, genome=genome_gen0_org1)
org2 = organism.Organism(xyz=xyz_gen0, genome=genome_gen0_org2)

gen1 = organism.Generation(org1=org1, org2=org2, index=0, time=time)

generation_list = [gen1]

for i in range(1, max_gen+1):
    generation_list.append(generation_list[len(generation_list) - 1].next_gen())


for i in range(len(generation_list)):
    generation_list[i].to_csv()
