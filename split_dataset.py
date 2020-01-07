import os
import random
import numpy as np
import math

dataset_dir = 'C:\\Users\\usr1\\python\\final project\\merged-filtered-candidate-data\\tokenized'
training_set_dir = dataset_dir + '\\training\\'
testing_set_dir = dataset_dir + '\\testing\\'

# split into 70% training and 30% testing data, keeping data distribution approximately equal
def split_dataset():
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

# Count the number of examples in each dataset (training v testing)
def count():
    training_counts = [0 for x in range(12)]
    i = 0
    for filename in os.listdir('C:\\Users\\usr1\\python\\final project\\merged-filtered-candidate-data\\tokenized\\training'):
        f = open('C:\\Users\\usr1\\python\\final project\\merged-filtered-candidate-data\\tokenized\\training\\' + filename)
        for line in f.readlines():
            training_counts[i] += 1
        i += 1

    test_counts = [0 for x in range(12)]
    i = 0
    for filename in os.listdir('C:\\Users\\usr1\\python\\final project\\merged-filtered-candidate-data\\tokenized\\testing'):
        f = open('C:\\Users\\usr1\\python\\final project\\merged-filtered-candidate-data\\tokenized\\testing\\' + filename)
        for line in f.readlines():
            test_counts[i] += 1
        i += 1


    print('training', training_counts, 'total:', sum(training_counts))
    print('testing', test_counts, 'total:', sum(test_counts))
    print('total', sum(training_counts) + sum(test_counts))

if __name__ == '__main__':
    split_dataset()
    count()