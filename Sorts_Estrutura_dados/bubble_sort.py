import time

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

data_sets = []

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

# Executando o Bubble sort para cada conjunto de dados
for i, data in enumerate(data_sets):
    inicio = time.time()
    sorted_data = bubble_sort(data)
    fim = time.time()
    tempo_total = fim - inicio

    # Imprimindo o resultado e o tempo de execução para cada iteração
    print(f"Iteração {i+1}:")
    print("Lista ordenada:", sorted_data)
    print(f"Tempo de execução Iteração {i+1}:", tempo_total, "segundos")
    print()

