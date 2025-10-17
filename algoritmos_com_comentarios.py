def fifo(sequencia, quadros): #declara função fifo que recebe a sequencia(lista de referências de página) e o numero de quadros da memoria
    memoria = [] #cria a lista que vai representar os quadros que estão ocupados
    ordem_entrada = [] #lista que guarda a ordem de chegada das paginas
    for pagina in sequencia: #para cada pagina na sequencia executa o loop
        if pagina in memoria:
            continue #se a pagina ja estiver na memoria, nao faz nada e passa para a proxima
        if len(memoria) < quadros: # se o tamanho da memoria for menor que os quadros
            memoria.append(pagina) #coloca a pagina em um quadro livre
            ordem_entrada.append(pagina) #registra a pagina que entrou agora
        else:
            pagina_substituida = ordem_entrada.pop(0) #remove a pagina que esntrou primeiro
            indice = memoria.index(pagina_substituida) #encontra a posição da pagina na lista de memoria pra saber onde sobrescrever
            memoria[indice] = pagina #substitui a pagina que saiu pela nova pagina
            ordem_entrada.append(pagina) #adiciona a nova pagina na lista de ordem de entrada
    return memoria #retorna a lista de memoria e as paginas que ficaram nos quadros
        
def lru(sequencia, quadros): #declara função lru que recebe a sequencia(lista de referências de página) e o numero de quadros da memoria
    memoria = [] #lista que guarda as paginas atualmente nos quadros
    ultimo_uso = {} #dicionario que guarda a ultima vez que cada pagina foi usada
    tempo = 0 #marca temporal
    for pagina in sequencia:
        tempo += 1 #cada pagina tem uma marcação temporal unica e isso vai incrementando
        if pagina in memoria:
            ultimo_uso[pagina] = tempo #atualiza o tempo de uso da pagina
            continue #se a pagina ja estiver na memoria, nao faz nada e passa para a proxima
        if len(memoria) < quadros: # se o tamanho da memoria for menor que os quadros
            memoria.append(pagina) #coloca a pagina em um quadro livre
            ultimo_uso[pagina] = tempo #registra o tempo de uso da pagina
        else:
            lru_pagina = min(memoria, key=lambda x: ultimo_uso.get(x, 0)) #busca na lista de memoria a pagina com menor valor no ultimo_uso
            indice = memoria.index(lru_pagina) #encontra a posição da pagina na lista de memoria pra saber onde sobrescrever
            memoria[indice] = pagina #substitui a pagina que saiu pela nova pagina
            ultimo_uso[pagina] = tempo #atualiza o tempo de uso da nova pagina
    return memoria

def mru(sequencia, quadros): 
    memoria = [] #lista da memoria
    ultimo_uso = {} #dicionario de ultimo uso
    tempo = 0#contador de tempo
    for pagina in sequencia:
        tempo += 1 #soma o tempo se a pagina esta na memoria e atualiza o ultimo uso
        if pagina in memoria:
            ultimo_uso[pagina] = tempo
            continue
        if len(memoria) < quadros: #se tem espaço na memoria, adiciona e marca tempo
            memoria.append(pagina)
            ultimo_uso[pagina] = tempo 
        else:
            mru_pagina = max(memoria, key=lambda x: ultimo_uso.get(x, 0)) #busca na lista de memoria a pagina com valor no ultimo_uso mais alto(por isso o max)
            indice = memoria.index(mru_pagina)
            memoria[indice] = pagina
            ultimo_uso[pagina] = tempo
    return memoria

def localizar_quadro(memoria, pagina):
    if pagina in memoria: #se a pagina estiver na memoria
        return memoria.index(pagina) + 1 #retorna o indice da pagina na memoria + 1 (para ficar mais amigavel para o usuario)
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

#2. Qual é o melhor algoritmo de substituição?
#O Ótimo é o melhor teoricamente porque substitui a página que será usada mais tarde no futuro, 
#resultando em menos faltas de página, mas é impossível de apicar na prática, porque sistema não 
# pode prever o futuro. O FIFO é simples de implementar, pois substitui a página mais antiga na memória,
# mas pode causar muitas faltas ao remover páginas ainda úteis. O LRU é eficiente porque se baseia no uso
#recente das páginas, removendo as menos usadas recentemente, o que reflete bem o comportamento real dos programs