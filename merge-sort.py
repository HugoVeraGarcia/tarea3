def merge_sort(items_list):
    if len(items_list) > 1:
        # Finding the mid of the items_list
        mid = len(items_list) // 2
        # Dividing the items_list elements into 2 halves
        left = items_list[:mid]
        right = items_list[mid:]

        # Sorting the first half
        merge_sort(left)
        # Sorting the second half
        merge_sort(right)

        i = 0  # nos ayuda a recorrer los elementos de la izquierda
        j = 0  # nos ayuda a recorrer los elementos de la derecha
        k = 0  # índice de la posición de la lista donde estamos mezclando

        while i < len(left) and j < len(right):  # mientras haya elementos en izquierda o derecha
            if left[i] < right[j]:  # si el elemento de la izquierda es menor
                items_list[k] = left[i]  # ponemos el menor elemento (en este caso el de la izquierda) en la posición k
                i += 1  # aumentamos j en 1 para continuar con el siguiente elemento o terminar con el while, si i llega a ser igual que la longitud de los elementos es porque ya pusiste todos los elementos en su lugar
            else:  # si el elemento de la derecha es menor (o si ambos son iguales)
                items_list[k] = right[j]  # ponemos el menor elemento (en este caso el de la derecha) en la posición k
                j += 1  # aumentamos j en 1 para continuar con el siguiente elemento o terminar con el while, si j llega a ser igual que la longitud de los elementos es porque ya pusiste todos los elementos en su lugar
            k += 1  # aumentamos k en 1 que es donde iría el siguiente elemento
            
        # * cuando hayas terminado con los elementos de una lista (en el while anterior), significa que todos los sobrantes de la otra lista van a la derecha

        # Metemos los elementos que hayan faltado de left
        while i < len(left):  # si hay algún elemento sobrante en la lista de la izquierda
            items_list[k] = left[i]
            i += 1  # aumentamos i en uno para continuar con el siguiente elemento o terminar el while
            k += 1  # aumentamos k en 1 que es donde iría el siguiente elemento

        # Metemos los elementos que hayan faltado de right
        while j < len(right):  # si hay algún elemento sobrante en la lista de la derecha
            items_list[k] = right[j]
            j += 1  # aumentamos j en uno para continuar con el siguiente elemento o terminar el while
            k += 1  # aumentamos k en 1 que es donde iría el siguiente elemento


items = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(items)
print(items)