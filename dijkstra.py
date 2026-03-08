# dijkstra.py
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.nodes[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes

# Function to reconstruct path from start to target
def shortest_path(previous_nodes, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path