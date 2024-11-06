import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def reconstruct_path(previous_nodes, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        if current == start:
            break
        current = previous_nodes[current]

    path.reverse()

    if path[0] == start:
        return path
    else:
        return []  # No path found

def get_user_input():
    graph = {}

    # Number of edges
    n = int(input("Enter the number of edges: "))

    # Build the graph from user input
    for _ in range(n):
        node1, node2, weight = input("Enter edge (node1 node2 weight): ").split()
        weight = int(weight)

        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []

        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))

    # Start and end node
    start_node = input("Enter the start node: ")
    end_node = input("Enter the end node: ")

    return graph, start_node, end_node

if __name__ == "__main__":
    graph, start_node, end_node = get_user_input()

    distances, previous_nodes = dijkstra(graph, start_node)

    print(f"Shortest distances from node {start_node}:")
    for node, distance in distances.items():
        print(f"  {node}: {distance}")

    path = reconstruct_path(previous_nodes, start_node, end_node)
    if path:
        print(f"\nShortest path from {start_node} to {end_node}: {' -> '.join(path)}")
    else:
        print(f"\nNo path exists from {start_node} to {end_node}.")