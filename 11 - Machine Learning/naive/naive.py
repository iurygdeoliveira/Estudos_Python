import numpy as np


def read_data():
    nl = np.float_(input().rsplit(' '))
    dl = []
    for i in np.arange(nl[0]-nl[1]):
        dl.append(input().replace('\r', '').rsplit(' '))

    train = np.vstack((dl))
    test = input().replace('\r', '').rsplit(' ')

    return train, test


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


train, test = read_data()

# Calculando a probabilidade do sim e do não
prob_nao, prob_sim, nao, sim = probabilidade(train[:, 4], 14)
# print("Probabilidade de sim e não em todo o DATASET")
# print("Sim: ", prob_sim, "Nao: ", prob_nao)
# print("Quantidade de Sim e Não em todo o DATASET")
#print("Sim: ", sim, "Não: ", nao)

# Calculando a probabilidade dos eventos
if(test[0] == "Ensolarado"):
    prob_aparencia_nao, prob_aparencia_sim = frequencia(
        train[:, [0, 4]], 'Ensolarado', sim, nao)
else:
    prob_aparencia_nao, prob_aparencia_sim = frequencia(
        train[:, [0, 4]], 'Chuvoso', sim, nao)

# print("Probabilidade do Evento Ensolarado")
# print("Sim: ", prob_ensolarado_sim)
# print("Nao: ", prob_ensolarado_nao)

prob_frio_nao, prob_frio_sim = frequencia(
    train[:, [1, 4]], 'Fria', sim, nao)

# print("Probabilidade do Evento Fria")
# print("Sim: ", prob_frio_sim)
# print("Nao: ", prob_frio_nao)

prob_alta_nao, prob_alta_sim = frequencia(
    train[:, [2, 4]], 'Alta', sim, nao)

# print("Probabilidade do Evento Alta")
# print("Sim: ", prob_alta_sim)
# print("Nao: ", prob_alta_nao)

if(test[3] == "Forte"):
    prob_vento_nao, prob_vento_sim = frequencia(
        train[:, [3, 4]], 'Forte', sim, nao)
else:
    prob_vento_nao, prob_vento_sim = frequencia(
        train[:, [3, 4]], 'Fraco', sim, nao)


# print("Probabilidade do Evento Forte")
# print("Sim: ", prob_forte_sim)
# print("Nao: ", prob_forte_nao)

v_sim = prob_sim * prob_aparencia_sim * \
    prob_frio_sim * prob_alta_sim * prob_vento_sim
v_nao = prob_nao * prob_aparencia_nao * \
    prob_frio_nao * prob_alta_nao * prob_vento_nao
# print("sim: ", round(v_sim, 3), "nao: ", round(v_nao, 3))

# normalizando
norm1 = v_sim/(v_sim + v_nao)
norm2 = v_nao/(v_nao + v_sim)

# print("Maior valor apos a normalização")
print("%.3f" % (max(norm1, norm2)))
