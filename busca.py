def busca_sequencial(v, x):
    i = 0

    while i < len(v):
        if v[i] == x:
            return i

        i += 1

    return -1

vetor = list(range(100,200))

print(vetor)
chave = 132
posicao = busca_sequencial(vetor, chave)
if posicao >= 0:
    print("o elemento %d foi encontrado na posição: %d" % (chave, posicao))
else:
    print('o elemento não foi encontrado')
