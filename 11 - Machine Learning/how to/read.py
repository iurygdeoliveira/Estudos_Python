import numpy as np


def read_file(name='../cases/naive.txt'):
    f = open(name, newline='')
    try:
        dataset = []
        reader = csv.reader(f, delimiter=' ', quotechar='|')
        for row in reader:
            dataset.append(row)
    finally:
        f.close()
    train = np.array(dataset[1:len(dataset)-1])
    test = np.array(dataset[len(dataset)-1])
    return train, test
