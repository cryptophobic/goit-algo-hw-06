import networkx as nx
import matplotlib.pyplot as plt
import conf

# Створення графа
G = nx.Graph()

# Додавання вузлів (зупинок/станцій)
G.add_nodes_from(conf.nodes)
G.add_weighted_edges_from(conf.edges)

# Візуалізація графа
pos = nx.spring_layout(G, seed=20)
nx.draw(G, pos, with_labels=True, node_size=2500, font_size=10, font_weight='bold', width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Моя квартира")
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()  # Кількість вершин
num_edges = G.number_of_edges()  # Кількість ребер
degrees = dict(G.degree())  # Ступені вершин

# Виведення результатів
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступені вершин:")
for node, degree in degrees.items():
    print(f"  {node}: {degree}")