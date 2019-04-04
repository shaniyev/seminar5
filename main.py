from mygraph import Graph
from myalgorithm import kruskals_algorithm

with open('graph_50.txt') as f:
    l = f.readline()
    m = []
    for line in f:
        m.append([int(i) for i in line.split()])

cnt = 0
g = Graph()


weight = []
for i in range(len(m)):
    weight.append(m[i][len(m[i]) - 1])

for i in range(len(m[0]) - 1):
    g.add_vertex(i)


for j in range(len(m)):
    x = None
    y = None
    cnt = 0
    for i in range(len(m[0]) - 1):
        if cnt == 0 and m[j][i] == 1:
            x = i
            cnt = 1
            continue
        if m[j][i] == 1 and cnt == 1:
            y = i
            cnt = 2
        if cnt == 2:
            g.add_edge(x, y, weight[j])
            break

g.print_graph()
print('Vertices:', g.vertices())
print('Edges: ', g.edges())
print('Number of edges:', g.num_edges())
print('Number of vertices:', g.num_vertices())
print('Get vertex: ', g.get_vertex(2))
print('Get edge: ', g.get_edge(3, 2))
print('Get adjacents: ', g.adj_vertices(1))
print('Minimum Spanning Tree:')

print(kruskals_algorithm(g.get_data(), g.num_vertices()))



