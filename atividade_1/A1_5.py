# Aluno: Tiago Faustino de Siqueira
# Matrícula: 22102193
#
# 5. [Algoritmo de Floyd-Warshall] (2,0pts) 
# Crie um programa que recebe um arquivo de grafo como argumento. 
# O programa deverá exercutar o algoritmo de Floyd-Warshall e mostrar as distâncias para cada par de vértices na tela
# utilizando o formato do exemplo abaixo. Na saída, cada linha terá as distâncias para vértice na ordem crescente
# dos índices informados no arquivo de entrada.
#
# Padrão de entrada:
#
# 1:0,10,3,5
# 2:10,0,9,8
# 3:3,9,0,11
# 4:5,8,11,0

import sys
import A1_1 as a1_1
import manager as m

def W(grafo: a1_1.Grafo, u, v):
    if u == v:
        return 0
    return grafo.peso(u, v)

def floyd_warshall(grafo: a1_1.Grafo):
    vertices = list(grafo.vertices.values())  # Obtém a lista de objetos Vertice
    D_anterior = {}
    D = {u: {v: W(grafo, u, v) for v in vertices} for u in vertices}

    for k in vertices:
        D, D_anterior = D_anterior, D
        for u in vertices:
            for v in vertices:
                D_u = D.setdefault(u, {})
                D_u[v] = min(D_anterior[u][v], D_anterior[u][k] + D_anterior[k][v])

    return D

if __name__ == "__main__":
    filename = sys.argv[1]
    manager = m.Manager(file=filename, temPeso=True)
    grafo = manager.graph

    D = floyd_warshall(grafo)

    for v in grafo.vertices.values():
        linha = ",".join(str(D[v][u]) for u in grafo.vertices.values())
        print(f"{v.rotulo}: {linha}")