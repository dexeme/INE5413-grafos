# Aluno: Tiago Faustino de Siqueira
# Matrícula: 22102193
#
# 3. [Ciclo Euleriano] (2,0pts) Crie um programa que recebe um grafo como argumento. Ao final, o programa deverá
# determinar se há ou não um ciclo euleriano e exibi-lo na tela de acordo com o exemplo abaixo. A primeira linha
# deverá conter o número 0 caso o grafo não contenha o ciclo euleriano. Caso contenha, deverá ser impresso 1 na
# primeira linha e em seguida, a sequência de vértices que corresponde ao ciclo deverá ser impressa.
#
# Padrão de saída:
#
# 1
# 2,4,3,1,5,6,2

import sys
import A1_1 as a1_1
import manager as m

import sys
import A1_1 as a1_1
import manager as m

def is_connected(grafo: a1_1.Grafo):
    visited = set()
    start = next((v for v in grafo.vertices.values() if v.grau > 0), None)
    if not start:
        return False

    def dfs(v):
        visited.add(v)
        for neighbor in v.vizinhos:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return len(visited) == len([v for v in grafo.vertices.values() if v.grau > 0])


def has_eulerian_circuit(grafo: a1_1.Grafo):
    if not is_connected(grafo):
        return False
    return all(v.grau % 2 == 0 for v in grafo.vertices.values() if v.grau > 0)

def find_eulerian_circuit(grafo: a1_1.Grafo):
    if not has_eulerian_circuit(grafo):
        return [0]

    stack = []
    circuit = []
    current_vertex = next((v for v in grafo.vertices.values() if v.grau > 0), None)
    stack.append(current_vertex)

    while stack:
        if current_vertex.grau > 0:
            stack.append(current_vertex)
            next_vertex = next(iter(current_vertex.vizinhos))
            current_vertex.vizinhos.remove(next_vertex)
            next_vertex.vizinhos.remove(current_vertex)
            current_vertex.grau -= 1
            next_vertex.grau -= 1
            current_vertex = next_vertex
        else:
            circuit.append(current_vertex.rotulo)
            current_vertex = stack.pop()
    return circuit[::-1], 1

if __name__ == "__main__":
    filename = sys.argv[1]
    manager = m.Manager(file=filename, temPeso=True)
    circuito, answer = (find_eulerian_circuit(grafo=manager.graph))
    print(answer)
    for i in range(len(circuito)):
        if i == len(circuito) - 1:
            print(circuito[i])
        else:
            print(circuito[i], end=',')