import A1_1 as a1_1

class Manager:
    def __init__(self, file: str, temPeso: bool):
        self.file = file
        self.temPeso = temPeso
        self.vertices = []
        self.edges = []
        self.graph = a1_1.Grafo()
        self.read()

    def read(self):
        with open(self.file, 'r') as f:
            lines = f.readlines()
            # O número de vértices está na primeira linha após a palavra 'vertices'.
            num_vertices = int(lines[0].strip().split(' ')[1])
            print("Total de vértices: ", num_vertices)

            # As linhas dos vértices estão imediatamente após '*vertices n'.
            vertex_lines = lines[1:1 + num_vertices]
            
            # As arestas começam após as linhas dos vértices e o marcador '*edges'.
            edge_lines = lines[2 + num_vertices:]

            for line in vertex_lines:
                parts = line.strip().split(' ')
                self.graph.adicionar_vertice(parts[0])
            for line in edge_lines:
                parts = line.strip().split(' ')
                # Converta o peso para float.
                self.graph.adicionar_aresta(parts , self.temPeso)

