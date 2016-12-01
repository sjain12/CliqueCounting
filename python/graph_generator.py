import itertools
import sys
import triangle_counters
import numpy as np
import graph_tools
import random

def ER(vertices,prob,fname=''):
    
    G = graph_tools.graph()

    edges = 0
    for i in range(0,vertices):
        for j in range(i+1,vertices):
            if random.random() < prob:
                G.Add_und_edge(str(i),str(j))
                edges += 1

    if fname != '':
        f_ptr = open(fname,'w')
        f_ptr.write(str(vertices)+' '+str(edges)+'\n')

        for node in G.vertices:
            for nbr in G.adj_list[node]:
                if node < nbr:
                    f_ptr.write(str(node)+' '+str(nbr)+'\n')
    
    return G


