import itertools
import sys
import triangle_counters
import numpy as np


def wedge_collision(G,fname='',gname='',to_list=False):
    three_wed = 0
    diamond_wed = 0
    three_tri = 0
    wheel = 0
    five_clique = 0
    almost_clique = 0

    wedges = dict()
    for node1 in G.vertices:
        for (nbr1, nbr2) in itertools.combinations(G.adj_list[node1],2):
            if nbr2 > nbr1:
                swap = nbr1
                nbr1 = nbr2
                nbr2 = swap

#             print 'outer', node1, nbr1, nbr2
            if (nbr1,nbr2) not in wedges:
                wedges[(nbr1,nbr2)] = set({node1})
            else:
                wedges[(nbr1,nbr2)].add(node1)
#                 print 'adding', nbr1, nbr2, wedges[(nbr1,nbr2)]

    for pair in wedges.keys():
        num = len(wedges[pair])
        three_wed = three_wed + num*(num-1)*(num-2)/6

        if to_list:
            print pair, wedges[pair]

        if pair[0] in G.adj_list[pair[1]]:
            connected = True
        else:
            connected = False

        for (nbr1, nbr2, nbr3) in itertools.combinations(wedges[pair],3):
            num_edges = 0
            if to_list:
                print pair, nbr1, nbr2, nbr3
            if nbr1 in G.adj_list[nbr2]:
                num_edges += 1
            if nbr1 in G.adj_list[nbr3]:
                num_edges += 1
            if nbr2 in G.adj_list[nbr3]:
                num_edges += 1



            diamond_wed += num_edges
            wheel = wheel+ (num_edges*(num_edges-1))/2
            almost_clique += (num_edges*(num_edges-1)*(num_edges-2))/6
            
            if connected:
                three_tri += 1
                almost_clique += (num_edges*(num_edges-1))/2
                five_clique += (num_edges*(num_edges-1)*(num_edges-2))/6
#                 if num_edges == 3:
#                     dummy = [int(pair[0]), int(pair[1]), int(nbr1), int(nbr2), int(nbr3)]
#                     dummy = sorted(dummy)
#                     print "found from",pair[0],pair[1]
#                     print "clique", dummy[0], dummy[1], dummy[2], dummy[3], dummy[4]

#             print connected, num_edges

           
    wheel = wheel/2
    five_clique = five_clique/10
    almost_clique = almost_clique/4  

    return (three_wed, three_tri, wheel, diamond_wed, almost_clique, five_clique)


def four_path_based(G,fname='',gname='',to_list=False):
    
    tailed_cycle = 0
    hatted_cycle = 0

    tailed_clique = 0
    hatted_clique = 0

    for node1 in G.vertices:
        for node2 in G.adj_list[node1]:
            for node3 in G.adj_list[node2]:
                if node3 == node1:
                    continue
                for node4 in G.adj_list[node3]:
                    if node4 == node2 or node4 == node1:
                        continue;
                    for node5 in G.adj_list[node4]:
                        if node5 == node3 or node5 == node2 or node5 == node1:
                            continue
                        if G.isEdge(node2,node5):
                            tailed_cycle = tailed_cycle+1
                            if to_list:
                                print("Tailed cycle:",node1,node2,node3,node4,node5)
                            
                            if G.isEdge(node3,node5) and G.isEdge(node2,node4):
                                tailed_clique = tailed_clique+1
                                if to_list:
                                    print("Tailed clique:",node1,node2,node3,node4,node5)

                            if G.isEdge(node1,node3):
                                hatted_cycle = hatted_cycle+1
                                if to_list:
                                    print("Hatted cycle:",node1,node2,node3,node4,node5)

                                if G.isEdge(node3,node5) and G.isEdge(node2,node4):
                                    hatted_clique = hatted_clique+1
                                    if to_list:
                                        print("Hatted clique:",node1,node2,node3,node4,node5)

    return (tailed_cycle/2,hatted_cycle/2,tailed_clique/6,hatted_clique/4)


