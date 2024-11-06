from collections import defaultdict, deque

# Depth First Search (DFS) function with support for Pre-order, In-order, and Post-order traversals
def dfs_recursive(graph, node, traversal_type):
    visited = set()  # To keep track of visited nodes

    # Pre-order DFS: Visit node first, then recursively visit its neighbors
    def _dfs_preorder(node):
        if node not in visited:
            print(node, end=' ')  # Print the node (visit)
            visited.add(node)  # Mark the node as visited
            for neighbor in graph[node]:  # Recursively visit all neighbors
                _dfs_preorder(neighbor)

    # In-order DFS: Works for binary tree-like graphs (assuming two neighbors)
    def _dfs_inorder(node):
        if node not in visited:
            visited.add(node)
            neighbors = graph[node]
            if len(neighbors) > 1:  # Binary-like traversal if the node has two neighbors
                _dfs_inorder(neighbors[0])  # Traverse the left neighbor first
                print(node, end=' ')  # Print node (visit)
                _dfs_inorder(neighbors[1])  # Traverse the right neighbor
            elif len(neighbors) == 1:  # If only one neighbor, treat it as the left node
                _dfs_inorder(neighbors[0])
                print(node, end=' ')  # Print node (visit)
            else:  # If no neighbors, just print the node
                print(node, end=' ')

    # Post-order DFS: Visit neighbors first, then the node itself
    def _dfs_postorder(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:  # Recursively visit all neighbors first
                _dfs_postorder(neighbor)
            print(node, end=' ')  # Print node (visit)44

    # Based on the user's choice, call the appropriate DFS traversal function
    if traversal_type == 'preorder':
        print("DFS traversal (Preorder):")
        _dfs_preorder(node)
    elif traversal_type == 'inorder':
        print("DFS traversal (Inorder):")
        _dfs_inorder(node)
    elif traversal_type == 'postorder':
        print("DFS traversal (Postorder):")
        _dfs_postorder(node)
    else:
        print("Invalid traversal type")

# Breadth First Search (BFS) function
def bfs_algorithm(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Queue to manage nodes to visit in BFS order
    visited.add(start_node)  # Mark the starting node as visited

    while queue:
        node = queue.popleft()  # Get the next node from the queue
        print(node, end=' ')  # Print node (visit)

        # Add unvisited neighbors to the queue for future exploration
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Function to allow the user to dynamically create the graph
def create_graph():
    graph = defaultdict(list)  # Initialize graph as an adjacency list
    num_nodes = int(input("Enter the number of nodes: "))  # Get number of nodes

    # Get the node and its neighbors from user input
    for _ in range(num_nodes):
        node = input("Enter the node: ").strip()
        num_neighbors = int(input(f"Enter the number of neighbors for {node}: "))

        # Add each neighbor to the graph's adjacency list
        for _ in range(num_neighbors):
            neighbor = input(f"Enter the neighbor of {node}: ").strip()
            graph[node].append(neighbor)

    return graph

# Main function to run the program
def main():
    graph = create_graph()  # Create graph using user input

    # Create a mapping from index to node for easier selection in the menu
    index_to_node = {i: node for i, node in enumerate(graph.keys())}

    # Continuously show menu options until the user exits
    while True:
        print("\nMenu:")
        print("1. Perform DFS")
        print("2. Perform BFS")
        print("3. Exit")

        # Try to get user input and handle invalid choices
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        # If the user selects DFS
        if choice == 1:
            print("\nSelect starting node for DFS:")
            for i, node in index_to_node.items():
                print(f"{i}. {node}")

            try:
                start_node_index = int(input("Enter index of starting node: "))
                start_node = index_to_node.get(start_node_index)

                if start_node is None:
                    print("Invalid index. Please select a valid index.")
                    continue

                print("\nDFS Traversal Options:")
                print("1. Preorder")
                print("2. Inorder")
                print("3. Postorder")
                traversal_choice = int(input("Enter your choice for DFS traversal type: "))

                # Perform the selected DFS traversal type
                if traversal_choice == 1:
                    dfs_recursive(graph, start_node, 'preorder')
                    print()
                elif traversal_choice == 2:
                    dfs_recursive(graph, start_node, 'inorder')
                    print()
                elif traversal_choice == 3:
                    dfs_recursive(graph, start_node, 'postorder')
                    print()
                else:
                    print("Invalid traversal type choice. Please enter 1, 2, or 3.")

            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

        # If the user selects BFS
        elif choice == 2:
            print("\nSelect starting node for BFS:")
            for i, node in index_to_node.items():
                print(f"{i}. {node}")

            try:
                start_node_index = int(input("Enter index of starting node: "))
                start_node = index_to_node.get(start_node_index)

                if start_node is None:
                    print("Invalid index. Please select a valid index.")
                    continue

                print("\nBFS traversal:")
                bfs_algorithm(graph, start_node)
                print()

            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

        # Exit the program if the user chooses option 3
        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Entry point of the script
if __name__ == "__main__":
    main()