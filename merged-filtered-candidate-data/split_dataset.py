import os
import random
import numpy as np
import math

dataset_dir = 'C:\\Users\\usr1\\python\\final project\\merged-filtered-candidate-data\\tokenized'
training_set_dir = dataset_dir + '\\training\\'
testing_set_dir = dataset_dir + '\\testing\\'

for filename in os.listdir(dataset_dir):
    if filename[-4:] == '.txt':
        print(filename)
        f = open(dataset_dir + '\\' + filename, 'r')
        g = open(training_set_dir + filename, 'w+')
        h = open(testing_set_dir + filename, 'w+')
        lines = f.readlines()
        random.shuffle(lines)
        # put ~70 and ~30% in each, normal dist centered at 70% with 8$ stddev
        break_point = math.floor(np.random.normal(len(lines) * 70 / 100, len(lines) * 8 / 100))
        g.writelines(lines[:break_point])
        h.writelines(lines[break_point:])
        g.close()
        h.close()
        f.close()
