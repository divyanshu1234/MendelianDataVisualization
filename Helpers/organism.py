import pandas as pd

from Helpers import helper


class Organism(object):
    def __init__(self, xyz, genome):
        self.xyz = xyz
        self.genome = genome
        self.transform_genes()

    def transform_genes(self):
        for i in range(0, len(self.genome), 2):
            a1 = self.genome[i]
            a2 = self.genome[i + 1]

            if a1.isupper() or a2.isupper():
                self.xyz = helper.transform(self.xyz, a1.upper())


class Generation(object):
    def __init__(self, org1, org2, index, time):
        self.org1 = org1
        self.org2 = org2
        self.index = index
        self.time = time

    def next_gen(self):
        genome_next1 = ""
        genome_next2 = ""
        for i in range(0, len(self.org1.genome), 2):
            genome_next1 = genome_next1 + helper.get_random_allele_pair(self.org1.genome[i: i + 2], self.org2.genome[i: i + 2])
            genome_next2 = genome_next2 + helper.get_random_allele_pair(self.org1.genome[i: i + 2], self.org2.genome[i: i + 2])

        xyz_next_1 = (self.org1.xyz + self.org2.xyz) / 2
        xyz_next_2 = (self.org1.xyz - self.org2.xyz) / 2
        org_next1 = Organism(xyz=xyz_next_1, genome=genome_next1)
        org_next2 = Organism(xyz=xyz_next_2, genome=genome_next2)

        print(genome_next1)
        print(genome_next2)

        return Generation(org1=org_next1, org2=org_next2, index=(self.index+1), time=self.time)

    def to_csv(self):
        output_dict = {
            'time': self.time,
            'org1_x': self.org1.xyz[:, 0],
            'org1_y': self.org1.xyz[:, 1],
            'org1_z': self.org1.xyz[:, 2],
            'org2_x': self.org2.xyz[:, 0],
            'org2_y': self.org2.xyz[:, 1],
            'org2_z': self.org2.xyz[:, 2]
        }

        output_dataframe = pd.DataFrame(output_dict)
        output_dataframe.to_csv("Outputs/Generations/generation_" + str(self.index) + ".csv")
