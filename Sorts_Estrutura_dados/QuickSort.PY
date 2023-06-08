import time

def particao(array, baixo, alto):
    pivô = array[alto]
    i = baixo - 1

    for j in range(baixo, alto):
        if array[j] <= pivô:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[alto]) = (array[alto], array[i + 1])

    return i + 1

def quickSort(array, baixo, alto):
    if baixo < alto:
        pi = particao(array, baixo, alto)
        quickSort(array, baixo, pi - 1)
        quickSort(array, pi + 1, alto)

data_sets = []

# Lista dos nomes dos arquivos
file_names = [
    "num.1000.1.in", "num.1000.2.in", "num.1000.3.in", "num.1000.4.in",
    "num.10000.1.in", "num.10000.2.in", "num.10000.3.in", "num.10000.4.in",
    "num.100000.1.in", "num.100000.2.in", "num.100000.3.in", "num.100000.4.in"
]

# Ler os dados de cada arquivo e adicioná-los à lista de data_sets
for file_name in file_names:
    with open(file_name, "r") as file:
        lines = file.readlines()
        data = [int(line.strip()) for line in lines]
        data_sets.append(data)

# Executando o quick sort para cada conjunto de dados
for i, data in enumerate(data_sets):
    inicio = time.time()
    quickSort(data, 0, len(data) - 1)
    fim = time.time()
    tempo_total = fim - inicio

    # Imprimindo o resultado e o tempo de execução para cada iteração
    print(f"Iteração {i+1}:")
    print("Lista ordenada:", data)
    print(f"Tempo de execução Iteração {i+1}:", tempo_total, "segundos")
    print()
