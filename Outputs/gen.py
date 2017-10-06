import transforms3d.euler
import numpy as np


xyz = [1, 0, 0]

rot = transforms3d.euler.euler2mat(0, 0, np.pi / 2)

print(np.matmul(xyz, rot))
