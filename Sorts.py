#sección 1; Algoritmos de ordenamiento..
#a) Ordenamiento por shell (Shell sort).
def shell_sort(list):
    size = len(list)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            anchor = list[i]
            j = i
            while(list[j-gap]>anchor and j>=gap):
                list[j] = list[j-gap]
                j-=gap
            list[j]=anchor
        gap = gap//2
    return(list)

    # En el mejor caso (n log n), el arreglo ya está ordenado o casi ordenado, hay menos comparaciones y movimientos
    # En el peor caso (O(n²)), el arreglo está invertido, aumentando mucho los intercambios
    # En el caso promedio, el rendimiento está entre los dos,  O(n log n).

    #Mejor	Ω(n log n) el arreglo está casi ordenado
    #Promedio	Θ(n log n)
    #Peor	O(n²) el arreglo está en orden inverso


#b) Ordenamiento por selecci ́on (Selection sort).
def selection_sort(list):
    size=len(list)
    for i in range(size):
        min_index=i
        for j in range(min_index+1,size):
            if list[j]<list[min_index]:
                min_index=j
        if i!=min_index:
            list[i], list[min_index]= list[min_index], list[i]

    return (list)

    #El mejor caso es cuando la lista ya está ordenada en orden ascendente. no realiza ningún intercambio innecesario.

    #El peor es cuando la lista está ordenada en orden descendente.
    #debe de hacer el máximo número de intercambios posibles.

    #El caso promedio es cuando los elementos están en un orden aleatorio.
    #pero el tiempo de ejecución promedio se acerca al del peor caso entre más desorden haya.

    #las comparaciones son = n(n-1)/2

    #tiene una complejidad de O(N^2) en todos los casos, ya que las comparaciones son las mismas sea el mejor o el peor caso
    #solo cambian los intercambios



#c) Ordenamiento por conteo (Counting sort).
def counting_sort(list):
    max1 = max(list)

    lista_ordenada = [0] * len(list)
    lista_numeros = [0] * (max1 + 1)

    for num in list:
        lista_numeros[num] += 1

    for i in range(1, max1 + 1):
        lista_numeros[i] += lista_numeros[i - 1]

    for num in reversed(list):
        lista_ordenada[lista_numeros[num] - 1] = num
        lista_numeros[num] -= 1

    return lista_ordenada

    #El mejor caso es cuando todos los elementos de la lista son iguales,
    #porque el conteo es O(n), y el acomodo es O(n).

    #El peor caso es cuando el rango estre numeros es muy grande y n es bajo
    #porque la estructura la lista count[] será muy grande, aumentando el espacio

    #El caso promedio es similar al mejor caso, ya que el conteo y acumulado son siempre O(n + k)
    #nadamas que k no sea muy grande

    #O(N+K)
    #Cuando es muy grande su complejidad sube y puede llegar a ser O(N^2)

    #Conteo = O(n)
    #Acumulado =  O(k)
    #Volver a construir el arreglo = O(n)
    #Total: O(n + k)

    #peor caso: O(n + k) k es el valor maximo en la lista
    #mejor caso : O(n + k)
    #caso promedio: O(n + k) k es estable

    #el tiempo de ejecución crece linealmente con n cuando k es pequeño, pero se degrada si k es grande.

#d) Ordenamiento por radix (Radix sort).
#radix sort utiliza counting sort como una subrutina para su ordenamiento
#hace su ordenamiento digito por digito desde los menos significativos a más significativos.
#ejecuta counting sort por cada digito.
def radix_sort(list):
    def counting_sort_radix(list,exp1):
        n = len(list)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = list[i] // exp1
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = list[i] // exp1
            output[count[index % 10] - 1] = list[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            list[i] = output[i]

    max1=max(list)

    exp1 = 1
    while max1/exp1>=1:
        counting_sort_radix(list,exp1)
        exp1*=10

    return (list)

    #En el mejor caso para radix sort es cuando el arreglo ya está ordenado.
    #pero aún debe completar todas las ejecuciones de counting sort, aunque el arreglo ya esté ordenado.

    #El peor caso es cuando los números están invertidos, todos los countingSort que se haran de manera menos eficiente

    #el caso promedio este algoritmo se acerca más al peor caso,porque hace el mimso numeor de operaciones
    #dependiendo de la cantidad de digitos más grande

    #radix hace tantas ejecuciones de counting como digitos haya en el numero más grande = b
    #counting sort tiene una complejidad de O(n+k) k=10 porque son digitos.
    #si los numeros son de tamaño similar la complejidad seria de O(b*(N+10)) = O(b*(N))

    #mejor, peor y caso promedio = O(b*(N+10)) = O(b*(N))

#e) Ordenamiento por intervalos (Bucket sort).
def bucket_sort(list):

        # Encontrar el valor máximo y mínimo para normalizar los datos
    min_val = min(list)
    max_val = max(list)
    bucket_range = (max_val - min_val) / len(list)  # Rango de cada bucket

    # Crear buckets vacíos
    buckets = [[] for _ in range(len(list))]

    # Colocar elementos en los buckets correspondientes
    for num in list:
        index = int((num - min_val) / bucket_range) if bucket_range > 0 else 0
        if index == len(list):  # Manejo de valores en el límite superior
            index -= 1
        buckets[index].append(num)

    # Ordenar cada bucket individualmente e insertar de nuevo en el array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # Usando sorted() (puede ser cambiado por otro algoritmo)

    return list
    #el mejor caso es cuando los elementos están distribuidos de manera ordenada en los cubos,
    #y cada cubo contiene solo un elemento o un número más pequeño.
    #Asi el proceso solo hace la inserción de los elementos en los cubos y despue slos acomoda en arreglo
    #sin necesidad de hacer un ordenamiento adentro, complejidad temporal de O(n).

    #El peor caso ocurre cuando todos los elementos están en un solo cubo,
    #lo que obliga a utilizar un algoritmo de ordenamiento interno peor.
    #este escenario tiene una complejidad de O(n²)

    #el caso promedio es cuando los datos están acomodados aleatoreamente
    #y ordenarlos internamente es más facil. complejidad de O(n + k log k)

    #mejor casi O(N)
    #peor caso O(N^2)
    #promedio O(N+KlogK)

    #el rendimiento de este algoritmo depende del acomodo de los datos
    #en la mayoría de los casos, el rendimiento se acerca a O(n), validando el análisis a priori.



list=[170,45,75,90,802,24,2,66]
print(counting_sort(list))
print(radix_sort(list))
print(shell_sort(list))
print(selection_sort(list))
print(bucket_sort(list))