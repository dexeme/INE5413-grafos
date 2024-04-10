# Aluno: Tiago Faustino de Siqueira
# Matrícula: 22102193
#
# [Buscas] (2.0pts) Crie um programa que receba um arquivo de grafo e o índice do vértice s como argumentos. O
# programa deve fazer uma busca em largura a partir de s e deverá imprimir a saída na tela, onde cada linha deverá
# conter o nível seguido de ":" e a listagem de vértices encontrados naquele nível. O exemplo abaixo trata de uma
# saída, na qual a busca se iniciou pelo vértice s no nível 0, depois prosseguiu nos vértices 3, 4 e 5 para o próximo
# nível. No próximo nível, a busca encontrou os vértices 1, 2, 6 e 7.
#
# Observações: Ignore os pesos do arquivo de entrada, pois a busca n˜ao precisar´a deles.
#
# Padrão de entrada:
# 0: 8
# 1: 3,4,5
# 2: 1,2,6,7

import sys
import A1_1 as a1_1
import manager as m

def buscaLargura(grafo: a1_1.Grafo, s: str):
    # A configuração de todos os vértices já foi feita no construtor

    # Configurando o vértice de origem
    try:
        grafo.vertices[s].visitado = True
        grafo.vertices[s].distancia = 0
    except KeyError:
        print("Vértice inicial não encontrado")
        return
    fila = [s] # Fila de vértices visitados, já inclui o vértice de origem
    nivel_agrupado = {} # Dicionário para agrupar os vértices por nível
    while fila:
        u = fila.pop(0)
        dist = grafo.vertices[u].distancia
        if dist not in nivel_agrupado:
            nivel_agrupado[dist] = []
        nivel_agrupado[dist].append(grafo.vertices[u].rotulo)
        for v in grafo.vizinhos(grafo.vertices[u]):
            if not v.visitado:
                v.visitado = True
                v.distancia = grafo.vertices[u].distancia + 1
                v.anterior = u
                fila.append(v.rotulo)

    for dist in sorted(nivel_agrupado):
        print(f"{dist}: {', '.join(nivel_agrupado[dist])}")
    
if __name__ == "__main__":
    filename = sys.argv[1]
    s = sys.argv[2] # Vértice que vai fazer a busca
    manager = m.Manager(file=filename, temPeso=False) # Não tem peso na busca em largura
    buscaLargura(grafo=manager.graph, s=s)