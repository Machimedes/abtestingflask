import networkx as nx
from matplotlib import pyplot as plt

G = nx.DiGraph()

[G.add_node(k) for k in ["A", "B", "C", "D", "E", "F", "G"]]
G.add_edges_from([('G', 'A'), ('A', 'G'), ('B', 'A'),
                  ('C', 'A'), ('A', 'C'), ('A', 'D'),
                  ('E', 'A'), ('F', 'A'), ('D', 'B'),
                  ('D', 'F')])

ppr1 = nx.pagerank(G)

print("Page rank value: " + str(ppr1))
pos = nx.spiral_layout(G)
nx.draw(G, pos, with_labels=True, node_color="#f86e00")
plt.show()
