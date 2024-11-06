import sys

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Prim's Algorithm
def prim_mst(graph):
    num_vertices = len(graph)
    selected = [False] * num_vertices
    mst_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    selected[0] = True
    num_edges = 0
    while num_edges < num_vertices - 1:
        min_edge = sys.maxsize
        u = v = -1
        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if not selected[j] and graph[i][j]:
                        if min_edge > graph[i][j]:
                            min_edge = graph[i][j]
                            u, v = i, j
        
        if u != -1 and v != -1:
            selected[v] = True
            mst_matrix[u][v] = graph[u][v]
            mst_matrix[v][u] = graph[v][u]
            num_edges += 1
    return mst_matrix

def print_matrix(matrix):
    print("MST Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

# Kruskal's Algorithm
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []  

    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        else:
            parent[i] = self.find(parent, parent[i])
            return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        mst = []
        self.graph.sort()  # Sort all edges in non-decreasing order of weight
        parent = list(range(self.V))
        rank = [0] * self.V
        for w, u, v in self.graph:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                mst.append((u, v, w))
                self.union(parent, rank, root_u, root_v)
        total_weight = sum(w for _, _, w in mst)
        return mst, total_weight

# Main Menu
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Selection Sort")
        print("2. Prim's Algorithm")
        print("3. Kruskal's Algorithm")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            sorted_arr = selection_sort(arr)
            print("Sorted array:", sorted_arr)

        elif choice == '2':
            num_vertices = int(input("Enter the number of vertices: "))
            graph = [[0] * num_vertices for _ in range(num_vertices)]
            num_edges = int(input("Enter the number of edges: "))
            print("Enter the edges in the format: vertex1 vertex2 weight")
            for _ in range(num_edges):
                u, v, weight = map(int, input().split())
                graph[u][v] = weight
                graph[v][u] = weight
            mst_matrix = prim_mst(graph)
            print_matrix(mst_matrix)

        elif choice == '3':
            try:
                vertices = int(input("Enter number of vertices: "))
                g = Graph(vertices)
                num_edges = int(input("Enter number of edges: "))
                for _ in range(num_edges):
                    u, v, w = map(int, input("Enter edge (u v w): ").split())
                    if u < 0 or v < 0 or u >= vertices or v >= vertices:
                        print("Error: Vertex indices must be within the range of vertices.")
                        return
                    g.add_edge(u, v, w)
                mst, total_weight = g.kruskal_mst()
                print("\nEdges in the MST:", mst)
                print("Total weight of the MST:", total_weight)
            except ValueError:
                print("Invalid input. Please enter integers only.")

        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()