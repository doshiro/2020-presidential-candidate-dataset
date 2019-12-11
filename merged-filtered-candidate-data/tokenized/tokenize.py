import os

def char_type(char):
    if char.isalpha(): return 1
    if char.isdigit(): return 2
    else: return 3

def tokenize(line):
    new_line = []
    for word in line.split():
        if(word.isalpha() or word.isdigit()):
            new_line.append(word)
        else:
            new_words = []
            curr_type = char_type(word[0])
            new_word = ""
            for char in word:
                if(char_type(char) == curr_type):
                    new_word += char
                else:
                    new_words.append(new_word)
                    new_word = "" + char
                    curr_type = char_type(char)
            new_words.append(new_word)

            for word in new_words:
                new_line.append(word)
    return ' '.join(new_line)

dataset_dir = 'C:\\Users\\usr1\\python\\final project\\merged-filtered-candidate-data'
for filename in os.listdir(dataset_dir):
    f = open(dataset_dir + '\\' + filename, 'r')
    g = open(dataset_dir + '\\tokenized\\' + filename, 'w+')
    for line in f.readlines():
        g.write(tokenize(line) + '\n')