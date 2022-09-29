import numpy as np
from igraph import *

def main():
    graph = Graph.Read_Ncol('myTree.ncol', directed= False)

    forest = []
    for vertex in graph.vs:
        newTree = []
        newTree.append(vertex)
        forest.append(newTree)      # Cada vertex vira uma floresta(lista) dentro da lista

    a = []                      # Arestas adicionadas
    i = 0
    while len(a) < len(forest[i]):
        for t in range(forest[i]):
            value = np.inf
            for f in forest and f != forest[i]:     # Para cada floresta na lista e
                                                    # essa floresta é diferente da atual
                for edge in graph.es:
                    if edge.source == forest[i][0]:
                        if forest[i] < value:


        i += 1


if __name__ == '__main__':
    main()