import os

def filter(filename):
    f = open(filename, 'r')
    g = open('filtered\\' + filename, 'w+')
    lines = f.readlines()
    for x in lines:
        if (len(x) > 1):
            g.write(x)
    f.close()
    g.close()

for filename in os.listdir(os.getcwd()):
    if (filename != 'filter.py' and filename != 'filtered'):
        filter(filename)