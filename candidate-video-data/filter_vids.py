import os

def goodword(word):
    return '[' not in word and ':' not in word

def filterfile(filename):
    f = open(filename, 'r')
    g = open('filtered\\' + filename, 'w+')
    lines = f.readlines()
    for x in lines:
        g.write(' '.join(list(filter(goodword,x.split()))) + '\n')
    f.close()
    g.close()

for filename in os.listdir(os.getcwd()):
    if (filename != 'filter_cids.py' and filename != 'filtered'):
        print(filename)
        filterfile(filename)