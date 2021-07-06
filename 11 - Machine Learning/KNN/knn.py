import numpy as np


def read_data():
    nl = np.float_(input().split(' '))
    dl = []
    for i in np.arange(nl[0]-nl[1]):
        dl.append(np.float_(input().split(' ')))

    train = np.vstack((dl))
    test = np.float_(input().split(' '))

    return train, test


train, test = read_data()

# Separando variáveis preditoras e variável target
X = train[:, :3]
Y = train[:, 3]
Y = np.array(Y)
X = np.array(X)


def shuffle_split_data(X, Y):
    arr_rand = np.random.rand(X.shape[0])
    split = arr_rand < np.percentile(arr_rand, 70)

    X_train = X[split]
    y_train = Y[split]
    X_test = X[~split]
    y_test = Y[~split]

    return X_train, y_train, X_test, y_test


# Separando os dados em conjuntos de treino e teste
X_train, Y_train, X_test, Y_test = shuffle_split_data(
    X, Y)


def distancia_euclidiana(att1, att2):
    dist = 0
    for i in range(len(att1)):
        dist += pow((att1[i] - att2[i]), 2)
    return np.sqrt(dist)


def KNN(array, k):

    # Array para o resultado final
    resultado = []

    # Loop por todos os elementos do array recebido como entrada
    for i in range(len(array)):
        valor = array[i]

        # Votação
        def vote(item):
            val = []
            for i in range(len(knn)):
                temp = item[i][1]
                val.append(temp)
            class_val = max(set(val), key=val.count)
            return class_val

        # Aplicando a função de distância aos dados
        distance = []
        for j in range(len(X_train)):

            # Calcula a distância de cada ponto de dado de entrada (array) para cada ponto de dado de treino
            euclidean_distance = distancia_euclidiana(valor, X_train[j])

            # Cria uma lista contendo a distância calculada e o valor do label do dado de treino em j
            temp = [euclidean_distance, Y_train[j]]

            # Adiciona o item anterior à lista de distâncias
            distance.append(temp)

        # Ordena
        distance.sort()

        # Obtém o valor de k para os vizinhos mais próximos
        knn = distance[:k]

        # Faz a votação
        resultado.append(vote(knn))
    return resultado


previsao = KNN([test], 5)
print(previsao[0])
