import numpy as np
from igraph import *

def main():
    graph = Graph.Read_Ncol('myGraph.ncol', directed=False)

    edges = []
    newEdge = None
    i = 0
    while i < len(graph.vs):        # Para cada arvore na lista
        for vi in graph.vs:         # Para cada vertice i nessa arvore
            add = False
            value = np.inf
            for edge in graph.es:   # Encontra a aresta de menor peso partindo de i para j
                if edge.source == vi.index and edge.target != vi.index and edge['weight'] < value:
                    value = edge['weight']
                    newEdge = edge
                    add = True
            if add:
                if not newEdge in edges:
                    edges.append(newEdge)
        i += 1

    print('*'*5 + ' Paths ' + '*'*5)
    for i in range(0, len(edges)):
        print(f'{edges[i].source} -> {edges[i].target}')
    print('*'*17)


if __name__ == '__main__':
    main()