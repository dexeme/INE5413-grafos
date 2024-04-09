# Aluno: Tiago Faustino de Siqueira
# Matrícula: 22102193
#
# 1. [Representação] (2,0pts) Crie um tipo estruturado de dados ou uma classe que represente um grafo não-direcionado
# e ponderado G(V, E, w), em que V é o conjunto de vértices, E é o conjunto de arestas e w: E → R é a função que
# mapeia o peso de cada aresta {u, v} ∈ E. As operações/métodos contemplados para o grafo devem ser:
# • qtdVertices(): retornar a quantidade de vértices;
# • qtdArestas(): retornar a quantidade de arestas;
# • grau(v): retornar o grau do vértice v;
# • rotulo(v): retornar o rótulo do vértice v;
# • vizinhos(v): retornar os vizinhos do vértice v;
# • haAresta(u, v): se {u, v} ∈ E, retornar verdadeiro; se não existir, retornar falso;
# • peso(u, v): se {u, v} ∈ E, retornar o peso da aresta {u, v}; se não existir, retornar um valor infinito positivo1;
# • ler(arquivo)2: deve carregar um grafo a partir de um arquivo no formato especificado ao final deste documento.
# IMPORTANTE: As operações/métodos devem ter complexidade de tempo computacional O(1) quando possível.
# No caso de dúvidas, consulte o professor da disciplina.
#
# Padrão de entrada:
# *vertices n
# 1 rotulo_de_1
# 2 rotulo_de_2
# ...
# n label_de_n
# *edges
# a b valor_do_peso
# a c valor_do_peso
# ...

import sys


class Vertice:
    def __init__(self, rotulo: str):
        self.rotulo = rotulo
        self.vizinhos = set()
        self.grau = 0

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = {}

    def qtdVertices(self):
        return len(self.vertices)
    
    def qtdArestas(self):
        # Cada aresta é contada duas vezes, então dividimos por 2.
        return len(self.arestas) // 2
    
    def grau(self, v: Vertice):
        return v.grau
    
    def rotulo(self, v: Vertice):
        return v.rotulo
    
    def vizinhos(self, v: Vertice):
        return v.vizinhos
    
    def haAresta(self, u: Vertice, v: Vertice):
        return (u, v) in self.arestas
    
    def peso(self, u: Vertice, v: Vertice):
        return self.arestas.get((u, v), float('inf'))
    
    def adicionar_vertice(self, rotulo: str):
        vertice = Vertice(rotulo)
        self.vertices[rotulo] = vertice

    def adicionar_aresta(self, u: str, v: str, peso: float):
        #print("Adicionando aresta entre", u, "e", v, "com peso", peso)
        if u not in self.vertices or v not in self.vertices:
            if u not in self.vertices:
                print("Vértice", u, "não encontrado.")
            if v not in self.vertices:
                print("Vértice", v, "não encontrado.")
        u_vertice = self.vertices[u]
        v_vertice = self.vertices[v]
        
        # Atualize os vizinhos e graus.
        u_vertice.vizinhos.add(v_vertice)
        v_vertice.vizinhos.add(u_vertice)
        u_vertice.grau += 1
        v_vertice.grau += 1

        # Armazene a aresta com seu peso de forma bidirecional para acesso direto.
        self.arestas[(u_vertice, v_vertice)] = peso
        self.arestas[(v_vertice, u_vertice)] = peso



class Manager:
    def __init__(self, file):
        self.file = file
        self.vertices = []
        self.edges = []
        self.graph = Grafo()
        self.read()

    def read(self):
        with open(self.file, 'r') as f:
            lines = f.readlines()
            # O número de vértices está na primeira linha após a palavra 'vertices'.
            num_vertices = int(lines[0].strip().split(' ')[1])
            print("Total de vértices: ", num_vertices)

            # As linhas dos vértices estão imediatamente após '*vertices n'.
            vertex_lines = lines[1:1 + num_vertices]
            print("Linhas dos vértices: ", vertex_lines)
            # As arestas começam após as linhas dos vértices e o marcador '*edges'.
            edge_lines = lines[2 + num_vertices:]

            for line in vertex_lines:
                parts = line.strip().split(' ')
                self.graph.adicionar_vertice(parts[0])
                print("Adicionando vértice", parts[0])
            for line in edge_lines:
                parts = line.strip().split(' ')
                # Converta o peso para float.
                self.graph.adicionar_aresta(parts[0], parts[1], float(parts[2]))


if __name__ == "__main__":
    filename = sys.argv[1]
    manager = Manager(filename)
