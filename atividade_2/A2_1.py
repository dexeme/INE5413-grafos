from grafo import GrafoDirigido
import manager as m
import sys

def CFC(grafo: GrafoDirigido):
    C, T, A, F= buscaProfundidade(grafo, grafo.vertices())
    F_decrescente = list(key for key, value in sorted(F.items(), key=lambda item: item[1], reverse=True))
    grafo.inverter_arestas()
    Ct, Tt, At, Ft = buscaProfundidade(grafo, F_decrescente)

    return At

def buscaProfundidade(grafo: GrafoDirigido, ordem) -> tuple[dict[int, int], dict[int, int]]:
    C = set()
    T = {v: float("inf") for v in grafo.vertices()}
    F = {v: float("inf") for v in grafo.vertices()}
    A = {v: None for v in grafo.vertices()}
    
    tempo = 0

    def dfs_visit(v):
        nonlocal tempo

        C.add(v)
        tempo += 1
        T[v] = tempo

        for u in grafo.vizinhos(v):
            if u not in C:
                A[u] = v
                dfs_visit(u)

        tempo += 1
        F[v] = tempo

    for u in ordem:
        if u not in C:
            dfs_visit(u)

    return C, T, A, F

def calcular_componentes(antecessores: dict[int, int | None]):

    componentes = {v: {v,} for v in antecessores.keys()}

    for v, u in antecessores.items():
        if u is None:
            continue
    
        componente_v = componentes[v]
        componente_u = componentes[u]

        if componente_v is not componente_u:
            x = componente_v.union(componente_u)
            for y in x:
                componentes[y] = x
    
    resultado = []
    for componente in componentes.values():
        if componente not in resultado:
            resultado.append(componente)
    
    return resultado


if __name__ == "__main__":
    filename = sys.argv[1]
    manager = m.Manager(file=filename, temPeso=True)
    grafo = manager.graph
    antecessores = CFC(grafo)
    componentes = calcular_componentes(antecessores)
    print(
        "\n".join(
            ",".join(str(v) for v in componente)
            for componente in componentes
        )
    )