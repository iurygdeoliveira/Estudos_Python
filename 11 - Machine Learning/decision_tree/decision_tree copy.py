import numpy as np
import math
import csv


def read_file(name='tree_caso_1.txt'):
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

# def read_data():
#     nl = np.float_(input().rsplit(' '))
#     dl = []
#     for i in np.arange(nl[0]-nl[1]):
#         dl.append(input().replace('\r', '').rsplit(' '))

#     train = np.vstack((dl))
#     test = input().replace('\r', '').rsplit(' ')

#     return train, test


# class arvore(object):
#     def __init__(self, key, left=None, right=None):
#         self.key = key
#         self.left = left
#         self.right = right


def probabilidade(array, total):
    nao = 0
    sim = 0
    for item in array:
        if(item == 'nao'):
            nao = nao + 1
        if(item == 'sim'):
            sim = sim + 1
    return (nao/total), (sim/total), nao, sim


def frequencia(array, event, sim, nao):

    sim_event = 0
    nao_event = 0
    for item in array:
        if(item[0] == event):
            if(item[1] == 'nao'):
                nao_event = nao_event + 1
            if(item[1] == 'sim'):
                sim_event = sim_event + 1
    return (nao_event/nao), (sim_event/sim)


def entropia(prob_sim, prob_nao):
    return - (prob_sim * math.log2(prob_sim)) - (prob_nao * math.log2(prob_nao))


train, test = read_file()

# Calculando a probabilidade do sim e do não em todo o DATASET
prob_nao, prob_sim, nao, sim = probabilidade(train[:, 4], 14)
print("Probabilidade de sim e não em todo o DATASET")
print("Sim: ", prob_sim, "Nao: ", prob_nao)
print("Quantidade de Sim e Não em todo o DATASET")
print("Sim: ", sim, "Não: ", nao)

# Calculando a Entropia do dataset
Entropia_dataset = entropia(prob_sim, prob_nao)
print("Valor da entropia do dataset")
print(Entropia_dataset)

root = arvore(42)
print("Raiz: ", root.key)

root.left = arvore(10)
root.right = arvore(90)
print("Raiz: ", root.key)
print("Filho esquerdo: ", root.left.key)
print("Filho direito: ", root.right.key)

# root.left = arvore(10)
# print("Maior valor apos a normalização")
#print("%.3f" % (max(norm1, norm2)))
