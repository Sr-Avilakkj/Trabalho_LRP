def mensagem_1(lista):
    print('''===============================================================================================

Ola! Sou o programa que compara o tempo de alguns dos metodos de organizacao em Python.
Sendo eles:

- Bubble Sort
- Selection Sort
- Inserction Sort
- Counting Sort
- Merge Sort

===============================================================================================
''')

    print(f'Essa e a lista antes de personalizar:\n{lista}')
    print('''Agora vamos personaliza-la...''')


def bubble_sort(lista, mostrar_lista_organizada):
    # Loop principal do Bubble Sort
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                # Troca os elementos de posição
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    if mostrar_lista_organizada == 'S' or mostrar_lista_organizada == 's':
        print(f'Bubble Sort:\n{lista}')


def selection_sort(lista, mostrar_lista_organizada):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

    if mostrar_lista_organizada == 'S' or mostrar_lista_organizada == 's':
        print(f'Selection Sort:\n{lista}')


def insertion_sort(lista, mostrar_lista_organizada):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

    if mostrar_lista_organizada == 'S' or mostrar_lista_organizada == 's':
        print(f'Insertion Sort:\n{lista}')


def counting_sort(lista, mostrar_lista_organizada):
    max_val = max(lista)
    count = [0] * (max_val + 1)

    while len(lista) > 0:
        num = lista.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            lista.append(i)
            count[i] -= 1

    if mostrar_lista_organizada == 'S' or mostrar_lista_organizada == 's':
        print(f'Counting Sort:\n{lista}')


def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
