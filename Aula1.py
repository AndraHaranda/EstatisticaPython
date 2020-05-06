def media(lista):
    soma = 0
    for c in range(len(lista)):
        soma += lista[c]

    soma /= len(lista)
    return round(soma, 2)

def calculoAmplitudeTotal(lista):
    maximo = max(lista)
    minimo = min(lista)

    amplitude = maximo - minimo
    return amplitude

def calculoDesvioQuartilico(lista):
    tamanhoLista = (len(lista))

    Q1 = (tamanhoLista + 1) // 4
    Q2 = (tamanhoLista + 2) * 2 // 4
    Q3 = (tamanhoLista + 3) * 3 // 4

    desvioQuartilico = [Q1, Q2, Q3]
    return desvioQuartilico

lista  = [2, 3, 4, 5, 7, 6, -3, -5]
media = media(lista)
amplitude = calculoAmplitudeTotal(lista)
desvioQuartilico = calculoDesvioQuartilico(lista)

lista.sort()

print('Lista ordenada: {lista}\n'
        'Média: {media}\n'
        'Amplitude total: {amplitudeTotal}\n'
        'Desvio Quartilico: {desvioQuartilico}\n'
        'Valor Q1: {lista[desvioQuartilico[0]]}\n'
        'Valor Q2: {lista[desvioQuartilico[1]]}\n'
        'Valor Q3: {lista[desvioQuartilico[2]]}\n')