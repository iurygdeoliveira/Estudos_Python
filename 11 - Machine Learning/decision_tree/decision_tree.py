import numpy as np
import math
import csv


def read_data():
    nl = np.float_(input().rsplit(' '))
    dl = []
    for i in np.arange(nl[0] - nl[1]):
        dl.append(input().replace('\r', '').rsplit(' '))

    train = np.vstack((dl))
    test = input().replace('\r', '').rsplit(' ')

    return train, test


class arvore(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def probabilidade(array, total):
    nao = 0
    sim = 0
    for item in array:
        if (item == 'nao'):
            nao = nao + 1
        if (item == 'sim'):
            sim = sim + 1
    return (nao / total), (sim / total), nao, sim


def frequencia(array, event, sim, nao):

    sim_event = 0
    nao_event = 0
    for item in array:
        if (item[0] == event):
            if (item[1] == 'nao'):
                nao_event = nao_event + 1
            if (item[1] == 'sim'):
                sim_event = sim_event + 1
    return (nao_event / nao), (sim_event / sim)


def entropia(prob_sim, prob_nao):
    return -((prob_sim * math.log2(prob_sim)) +
             (prob_nao * math.log2(prob_nao)))


train, test = read_data()

# Calculando a probabilidade do sim e do não em todo o DATASET
prob_nao, prob_sim, nao, sim = probabilidade(train[:, 4], 14)
print("Probabilidade de sim e não em todo o DATASET")
print("Sim: ", prob_sim, "Nao: ", prob_nao)
print("Quantidade de Sim e Não em todo o DATASET")
print("Sim: ", sim, "Não: ", nao)

# Calculando a entropia do dataset
Entropia_dataset = entropia(prob_sim, prob_nao)
print("Valor da entropia do dataset")
print(Entropia_dataset)

# Calculando o Ganho de informação do vento
Entropia_vento_fraco = entropia(6 / 8, 2 / 8)
print("Entropia_vento_fraco", Entropia_vento_fraco)
Entropia_vento_forte = entropia(3 / 6, 3 / 6)
print("Entropia_vento_forte", Entropia_vento_forte)
GI_vento = Entropia_dataset - ((8 / 14) * Entropia_vento_fraco) - (
    (6 / 14) * Entropia_vento_forte)
print("Ganho de Informação do Tempo")
print(GI_vento)

# Calculando o Ganho de informação da Humidade
Entropia_humidade_alta = entropia(3 / 7, 4 / 7)
print("Entropia_humidade_alta", Entropia_humidade_alta)
Entropia_humidade_normal = entropia(6 / 7, 1 / 7)
print("Entropia_humidade_normal", Entropia_humidade_normal)
GI_humidade = Entropia_dataset - ((7 / 14) * Entropia_humidade_alta) - (
    (7 / 14) * Entropia_humidade_normal)
print("Ganho de Informação da Humidade")
print(GI_humidade)

# Calculando o Ganho de informação da Temperatura
Entropia_temperatura_quente = entropia(2 / 4, 2 / 4)
print("Entropia_temperatura_quente", Entropia_temperatura_quente)
Entropia_temperatura_moderada = entropia(4 / 6, 2 / 6)
print("Entropia_temperatura_moderada", Entropia_temperatura_moderada)
Entropia_temperatura_fria = entropia(3 / 4, 1 / 4)
print("Entropia_temperatura_fria", Entropia_temperatura_fria)
GI_temperatura = Entropia_dataset - (
    (4 / 14) * Entropia_temperatura_quente) - (
        (6 / 14) * Entropia_temperatura_moderada) - (
            (4 / 14) * Entropia_temperatura_fria)
print("Ganho de Informação da Temperatura")
print(GI_temperatura)

# Calculando o Ganho de informação da Tempo
Entropia_tempo_ensolarado = entropia(2 / 5, 3 / 5)
print("Entropia_tempo_ensolarado", Entropia_tempo_ensolarado)
Entropia_tempo_nublado = 0
print("Entropia_tempo_nublado", Entropia_tempo_nublado)
Entropia_tempo_chuva = entropia(3 / 5, 1 / 5)
print("Entropia_tempo_chuva", Entropia_tempo_chuva)
GI_tempo = Entropia_dataset - ((5 / 14) * Entropia_tempo_ensolarado) - (
    (4 / 14) * Entropia_tempo_nublado) - ((5 / 14) * Entropia_tempo_chuva)
print("Ganho de Informação do tempo")
print(GI_tempo)

#O atributo com maior ganho de informação é o tempo

root = arvore(42)
print("Raiz: ", root.key)

root.left = arvore(10)
root.right = arvore(90)
print("Raiz: ", root.key)
print("Filho esquerdo: ", root.left.key)
print("Filho direito: ", root.right.key)

root.left = arvore(10)
print("Maior valor apos a normalização")
print("%.3f" % (max(norm1, norm2)))
