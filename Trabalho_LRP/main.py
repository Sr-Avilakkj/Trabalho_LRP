import order_functions
import time
import random

lista = []
order_functions.mensagem_1(lista)

# Criacao de lista personalizada
n = int(input('Informe n (Tamanho da lista):\n'))
k = (int(input('Informe k (Limite dos valores dos elementos):\n')))

for count in range(n):
    lista.append(random.randint(0, k))

mostrar_lista = input('Deseja que seja mostrada a lista gerada? (S/N)\n')

# Print da lista criada
if mostrar_lista == 'S':
    print(f'\nLista Original:\n{lista}\n')

mostrar_lista_organizada = input('Deseja que seja mostrada a lista'
                                 ' organizada apos cada metodo? (S/N)\n')

# Utilizacao dos metodos de ordenamento com seu tempo
inicio = time.time()
order_functions.bubble_sort(lista, mostrar_lista_organizada)
fim = time.time()
tempo = (fim - inicio) * 1000
print(f'Tempo em milissegundos Bubble Sort: {tempo}')

inicio = time.time()
order_functions.selection_sort(lista, mostrar_lista_organizada)
fim = time.time()
tempo = (fim - inicio) * 1000
print(f'Tempo em milissegundos Selection Sort: {tempo}')

inicio = time.time()
order_functions.insertion_sort(lista, mostrar_lista_organizada)
fim = time.time()
tempo = (fim - inicio) * 1000
print(f'Tempo em milissegundos Insertion Sort: {tempo}')

inicio = time.time()
order_functions.counting_sort(lista, mostrar_lista_organizada)
fim = time.time()
tempo = (fim - inicio) * 1000
print(f'Tempo em milissegundos Counting Sort: {tempo}')

inicio = time.time()
order_functions.merge_sort(lista)
if mostrar_lista_organizada == 'S':
    print(f'Merge Sort;\n{lista}')
fim = time.time()
tempo = (fim - inicio) * 1000
print(f'Tempo em milissegundos Merge Sort: {tempo}')
