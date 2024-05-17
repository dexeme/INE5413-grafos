import sys
import manager as m
import grafo as g
from heapq import heappop, heappush, heapify

def prim(grafo: g.Grafo):
    r, *_ = grafo.vertices()

    A = {v: None for v in grafo.vertices()}
    K = {v: float("inf") for v in grafo.vertices()}

    K[r] = 0
    
    Q = [(K[v], v) for v in grafo.vertices()]
    heapify(Q)

    visitados = set()

    while len(Q):
        _, u = heappop(Q)

        if u in visitados:
            continue
        visitados.add(u)
        
        for v in grafo.vizinhos(u):
            peso = grafo.peso(u, v)

            if v not in visitados and peso < K[v]:
                A[v] = u
                K[v] = peso
                heappush(Q, (peso, v))

    return A

if __name__ == "__main__":
    filename = sys.argv[1]
    manager = m.Manager(file=filename, temPeso=True)
    grafo = manager.graph
    prim(grafo)

    A = prim(grafo)
    somatorio = 0
    lista = []

    for k, v in A.items():
        if v is None:
            continue
        somatorio += grafo.peso(v, k)
        lista.append(f"{str(k)}-{str(v)}")

    print(somatorio)
    print(', '.join(lista))