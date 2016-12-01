import graph_tools
import triangle_counters
import four_vertex_counters
import five_vertex_counters
import sys

# graphs = ['amazon0312.txt', 'soc-Slashdot0902.txt', 'email-Enron.txt', 'ca-AstroPh.txt', 'experimental_STRING.edges', 'cit-HepPh.txt', 'textmining_STRING.edges', 'facebook_combined.txt', 'p2p-Gnutella31.txt']

# graphs = ['coexpression_STRING.edges']

# graphs = ['CE-CX.txt', 'CE-GN.txt', 'CE-PG.txt', 'HS-CX.txt', 'HS-LC.txt', 'SC-CC.txt', 'SC-CX.txt', 'SC-HT.txt', 'DM-CX.txt', 'DR-CX.txt']

name = sys.argv[1]

print('processing',name)
G = graph_tools.graph()
G.Read_edges(name)
counts = five_vertex_counters.four_path_based(G,'','',False)

wedge_stuff =  five_vertex_counters.wedge_collision(G,'','',False)

print "tailed 4-cycle", counts[0]
print "hatted 4-cycle", counts[1]
print "three wedge collision", wedge_stuff[0]
print "three triangles collision", wedge_stuff[1]
print "tailed 4-clique", counts[2]
print "wheels", wedge_stuff[2]
print "diamond-wedge collision", wedge_stuff[3]
print "hatted 4-clique", counts[3]
print "almost clique", wedge_stuff[4]
print "five clique", wedge_stuff[5]

