import conf


def build_dict_graph_from_edges():
    gr = {}
    for start, finish, weight in conf.edges:
        if start not in gr:
            gr[start] = {}
        if finish not in gr:
            gr[finish] = {}
        gr[start][finish] = weight
        gr[finish][start] = weight

    return gr

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

# Приклад графа у вигляді словника
graph = build_dict_graph_from_edges()

# Виклик функції для вершини A
print(dijkstra(graph, 'Вулиця'))
