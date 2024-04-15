# Aluno: Tiago Faustino de Siqueira
# Matrícula: 22102193
#
# 4. [Algoritmo de Bellman-Ford ou de Dijkstra] (2,0pts) Crie um programa que recebe um arquivo de grafo como
# argumento e um v´ertice s. O programa dever´a executar o algoritmo de Bellman-Ford ou de Dijkstra e informar o
# caminho percorrido de s at´e todos os outros v´ertices do grafo e a distˆancia necess´aria. A sa´ıda dever´a ser impressa
# na tela de acordo com o exemplo abaixo. Cada linha representa o caminho realizado de s para o v´ertice da respectiva
# linha. Em cada linha, antes dos s´ımbolo “:” dever´a estar o v´ertice destino. `A direita de “:”, encontra-se o caminho
# percorrido de s at´e o v´ertice destino. Mais `a direita encontram-se os s´ımbolos “d=” seguidos da distˆancia necess´aria
# para percorrer o caminho.
#
# Padrão de entrada:
#
# 1: 2,3,4,1; d=7
# 2: 2; d=0
# 3: 2,3; d=4
# 4: 2,3,4; d=6
# 5: 2,3,5; d=8
#
# Anotações de aula:
# - O algoritmo de Dijkstra é mais eficiente que o de Bellman-Ford, mas o de Bellman-Ford é mais robusto.
# - O algoritmo de Dijsktra é "míope", pois ele não reconsidera a solução após achar um caminho.
# - Os vértices não podem ter peso negativo, pois o algoritmo de Dijkstra não funciona com pesos negativos.
# - É um algoritmo guloso. Critério: custo em relação ao vértice de origem.
#
# Algoritmo em Psedocódigo:
# Algoritmo 11: Algoritmo de Dijkstra.
# Input :um grafo G = (V,E,w : E → R*+), um vértice de origem s ∈ V
# 1 Dv ← ∞ ∀v ∈ V
# 2 Av ← null ∀v ∈ V
# 3 Cv ← false ∀v ∈ V % Visitado
# 4 Ds ← 0
# 5 while ∃v ∈ V (Cv = false) do  % Enquanto houver vértices não visitados
# 6     u ← arg minv∈V {Dv |Cv =false} % Argmin: retorna o >>>vértice<<< com menor custo. 
#                                        Então diferente da função min, que retorna o valor 
#                                        mínimo, o argmin retorna o índice do valor mínimo.
#                                       a eficiência do argmin.
#                                       PARA A IMPLEMENTAÇÃO: Pensar em uma forma de melhorar
#                                       essa linha 6. A sugestão do professor foi manter uma fila de
#                                       prioridades mínimas para mapear a distância estimada no lugar
#                                       de D.
#                                       Seria utilizada uma operação do tipo 
#                                       “EXTRACT-MIN” no lugar da que está na
#                                       linha 6, para encontrar o vértice com
#                                       a menor distância. Ao extraí-lo da estrutura de
#                                       prioridade, não mais seria necessário. 
#                                       Ideia: usar uma Heap de Fibonacci. Achei uma implementação
#                                       em Python nesse site: https://www.programiz.com/dsa/fibonacci-heap
#                                       Antes ao atualizar a tabela ele precisaria ser removido, 
#                                       agora, ele vê se precisa atualizar essa chave, checando se
#                                       o nodo da heap é menor que o nodo pai. Se for, ele faz a troca.
# 7     Cu ← true
# 8     foreach v ∈ N(u)+ :Cv =false do
# 9         if Cv = false and Dv > Du +w((u, v)) then % Verifica se o vizinho já tem 
# 10            Dv ← Du +w((u, v))
# 11            Av ← u % Define o ancestral do caminho
# 12 
# 13 return (D, A)