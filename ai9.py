import heapq

def a_star(graph, start, end, heuristic):
    # Priority queue to store the nodes to be explored, with their priority
    open_list = []
    heapq.heappush(open_list, (0, start))
   
    # Dictionaries to store the cost and the path
    g_cost = {start: 0}
    f_cost = {start: heuristic[start]}
    came_from = {start: None}
   
    while open_list:
        current_priority, current_node = heapq.heappop(open_list)
       
        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1], g_cost[end]
       
        for neighbor, weight in graph[current_node].items():
            tentative_g_cost = g_cost[current_node] + weight
           
            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost[neighbor] = tentative_g_cost + heuristic[neighbor]
                came_from[neighbor] = current_node
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))
   
    return None, float('inf')

def main():
    graph = {}
    heuristic = {}
    
    # User input to create the graph
    num_nodes = int(input("Enter the number of nodes: "))
    for _ in range(num_nodes):
        node = input("Enter node: ").strip()
        graph[node] = {}
        heuristic[node] = int(input(f"Enter heuristic value for {node}: "))
    
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, w = input("Enter edge (u v w): ").strip().split()
        w = int(w)
        graph[u][v] = w
        graph[v][u] = w  # Assuming undirected graph
    
    start = input("Enter the start node: ").strip()
    end = input("Enter the end node: ").strip()
   
    if start not in graph or end not in graph:
        print("Invalid start or end node.")
        return
   
    path, cost = a_star(graph, start, end, heuristic)
   
    if path:
        print(f"Shortest path: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print("No path found.")

if __name__ == "__main__":  
    main()