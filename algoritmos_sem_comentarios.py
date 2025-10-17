def fifo(sequencia, quadros):
    memoria = []
    ordem_entrada = []
    for pagina in sequencia:
        if pagina in memoria:
            continue
        if len(memoria) < quadros:
            memoria.append(pagina)
            ordem_entrada.append(pagina)
        else:
            pagina_substituida = ordem_entrada.pop(0)
            indice = memoria.index(pagina_substituida)
            memoria[indice] = pagina
            ordem_entrada.append(pagina)
    return memoria

def lru(sequencia, quadros):
    memoria = []
    ultimo_uso = {}
    tempo = 0
    for pagina in sequencia:
        tempo += 1
        if pagina in memoria:
            ultimo_uso[pagina] = tempo
            continue
        if len(memoria) < quadros:
            memoria.append(pagina)
            ultimo_uso[pagina] = tempo
        else:
            lru_pagina = min(memoria, key=lambda x: ultimo_uso.get(x, 0))
            indice = memoria.index(lru_pagina)
            memoria[indice] = pagina
            ultimo_uso[pagina] = tempo
    return memoria

def mru(sequencia, quadros):
    memoria = []
    ultimo_uso = {}
    tempo = 0
    for pagina in sequencia:
        tempo += 1
        if pagina in memoria:
            ultimo_uso[pagina] = tempo
            continue
        if len(memoria) < quadros:
            memoria.append(pagina)
            ultimo_uso[pagina] = tempo
        else:
            mru_pagina = max(memoria, key=lambda x: ultimo_uso.get(x, 0))
            indice = memoria.index(mru_pagina)
            memoria[indice] = pagina
            ultimo_uso[pagina] = tempo
    return memoria

def localizar_quadro(memoria, pagina):
    if pagina in memoria:
        return memoria.index(pagina) + 1
    return None

if __name__ == "__main__":
    quadros = 8
    seq1 = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
    seq2 = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
    seq3 = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]
    alvo1 = 7
    alvo2 = 11
    alvo3 = 11

    for i, (seq, alvo) in enumerate([(seq1,alvo1),(seq2,alvo2),(seq3,alvo3)], start=1):
        mem_fifo = fifo(seq, quadros)
        mem_lru = lru(seq, quadros)
        mem_mru = mru(seq, quadros)
        print(f"Sequência {i}:")
        print(" FIFO memória final:", mem_fifo, " quadro da página", localizar_quadro(mem_fifo, alvo))
        print(" LRU memória final:", mem_lru, " quadro da página", localizar_quadro(mem_lru, alvo))
        print(" MRU memória final:", mem_mru, " quadro da página", localizar_quadro(mem_mru, alvo))
        print()
