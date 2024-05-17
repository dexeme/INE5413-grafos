import sys
import manager as m

class Grafo:
    rotulos: dict[int, str]
    mapa_vizinhos: dict[int, set[int]]
    mapa_pesos: dict[frozenset[int], int]

    def __init__(self):
        self.rotulos = {}
        self.mapa_vizinhos = {}
        self.mapa_pesos = {}

    def vertices(self):
        return set(self.rotulos.keys())

    def arestas(self):
        return set(self.mapa_pesos.keys())

    def qtdVertices(self):
        return len(self.rotulos)

    def qtdArestas(self):
        return len(self.mapa_pesos)

    def grau(self, v):
        return len(self.mapa_vizinhos.get(v, set()))

    def rotulo(self, v):
        return self.rotulos.get(v)

    def vizinhos(self, v):
        return self.mapa_vizinhos.get(v, set())

    def hasAresta(self, u, v):
        return frozenset({u, v}) in self.mapa_pesos

    def peso(self, u, v):
        return self.mapa_pesos.get(frozenset({u, v}), 0)

    def adicionar_vertice(self, rotulo, index):
        if index in self.rotulos:
            raise ValueError(f"Vertice with index {index} already exists.")

        self.rotulos[index] = rotulo
        self.mapa_vizinhos[index] = set()

    def adicionar_aresta(self, u, v, w):
        key = frozenset({u, v})
        self.mapa_pesos[key] = w

        if not u in self.rotulos:
            self.adicionar_vertice(str(u), u)
        if not v in self.rotulos:
            self.adicionar_vertice(str(v), v)

        self.mapa_vizinhos[u].add(v)
        self.mapa_vizinhos[v].add(u)

    def inverter_arestas(self):
        novo_mapa_vizinhos = {}
        novo_mapa_pesos = {}

        for aresta, peso in self.mapa_pesos.items():
            u, v = aresta
            novo_mapa_pesos[frozenset({v, u})] = peso

        for v, vizinhos in self.mapa_vizinhos.items():
            novo_mapa_vizinhos[v] = set()

        for u, v in self.arestas():
            novo_mapa_vizinhos[v].add(u)
            novo_mapa_vizinhos[u].add(v)

        self.mapa_vizinhos = novo_mapa_vizinhos
        self.mapa_pesos = novo_mapa_pesos


class GrafoDirigido:
    rotulos: dict[int, str]
    mapa_vizinhos: dict[int, tuple[int, int]]
    mapa_pesos: dict[tuple[int, int], int]

    def __init__(self):
        self.rotulos = {}
        self.mapa_vizinhos = {}
        self.mapa_pesos = {}

    def vertices(self):
        return set(self.rotulos.keys())

    def arestas(self):
        return set(self.mapa_pesos.keys())

    def qtdVertices(self):
        return len(self.rotulos)

    def qtdArestas(self):
        return len(self.mapa_pesos)

    def grau(self, v):
        return len(self.mapa_vizinhos.get(v, set()))

    def rotulo(self, v):
        return self.rotulos.get(v)

    def vizinhos(self, v):
        return self.mapa_vizinhos.get(v, set())

    def hasAresta(self, u, v):
        return (u, v) in self.mapa_pesos

    def peso(self, u, v):
        return self.mapa_pesos.get((u, v), 0)

    def adicionar_vertice(self, rotulo, index):
        if index in self.rotulos:
            raise ValueError(f"Vertice with index {index} already exists.")

        self.rotulos[index] = rotulo
        self.mapa_vizinhos[index] = set()

    def adicionar_aresta(self, u, v, w):
        key = (u, v)
        self.mapa_pesos[key] = w

        if not u in self.rotulos:
            self.adicionar_vertice(str(u), u)
        if not v in self.rotulos:
            self.adicionar_vertice(str(v), v)

        self.mapa_vizinhos[u].add(v)

    def inverter_arestas(self):
        novo_mapa_vizinhos = {}
        novo_mapa_pesos = {}

        for aresta, peso in self.mapa_pesos.items():
            u, v = aresta
            novo_mapa_pesos[(v, u)] = peso

        for v, vizinhos in self.mapa_vizinhos.items():
            novo_mapa_vizinhos[v] = set()

        for u, v in self.arestas():
            novo_mapa_vizinhos[v].add(u)

        self.mapa_vizinhos = novo_mapa_vizinhos
        self.mapa_pesos = novo_mapa_pesos

if __name__ == "__main__":
    filename = sys.argv[1]
    manager = m.Manager(file=filename, temPeso=True)
