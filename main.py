# main.py
from graph import Graph
from dijkstra import dijkstra, shortest_path

g = Graph()

print("Enter edges in format: start end weight")
print("Type 'done' when finished")

while True:
    entry = input("Edge: ")
    if entry.lower() == 'done':
        break
    try:
        start, end, weight = entry.split()
        weight = int(weight)
        g.add_edge(start, end, weight)
    except:
        print("Invalid input. Format: start end weight (e.g., A B 5)")

start_node = input("Enter starting node: ")

distances, previous_nodes = dijkstra(g, start_node)

print(f"\nShortest distances from {start_node}")
for node, distance in distances.items():
    print(f"{node}: {distance}")

print(f"\nShortest paths from {start_node}")
for node in g.nodes:
    if node == start_node:
        continue
    path = shortest_path(previous_nodes, node)
    print(f"{start_node} -> {node}: {' -> '.join(path)}")