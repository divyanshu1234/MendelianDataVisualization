import transforms3d.euler as eu
import numpy as np
import random


def transform(xyz, allele):
    return trans_functions[allele](xyz, trans_data[allele])


def translate(xyz, translation_data):
    return xyz + translation_data


def rotate(xyz, rot_data):
    out = []

    for i in range(len(xyz)):
        rotation = rot_data[i]
        rot_matrix = eu.euler2mat(rotation[0], rotation[1], rotation[2])
        out.append(np.matmul(xyz[i], rot_matrix))

    return np.array(out)


def scale(xyz, scale_data):
    out = []
    for i in range(len(scale_data)):
        out.append(xyz[i] * scale_data[i])

    return np.array(out)


def get_random_allele_pair(p1, p2):
    pair_list = [(p1[0] + p2[0]), (p1[0] + p2[1]), (p1[1] + p2[0]), (p1[1] + p2[1])]
    return pair_list[random.randint(0, 3)]


trans_functions = {
    'A': translate,
    'R': rotate,
    'I': scale
}

trans_data = {
    'A': [],
    'R': [],
    'I': []
}
