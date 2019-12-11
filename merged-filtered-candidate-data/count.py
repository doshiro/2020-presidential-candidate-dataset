import os

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
