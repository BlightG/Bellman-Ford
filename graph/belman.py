class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []    # List to store graph edges

    # Function to add an edge
    def add_edge(self, u, v, weight):
        edge = sorted([u, v])
        edge.append(weight)
        self.edges.append(edge)

    # Bellman-Ford algorithm to find the shortest path from the source
    def bellman_ford(self, source):
        # Step 1: Initialize distances from the source to all other vertices as infinity and source to 0
        dist = [float("Inf")] * self.V
        dist[source] = 0
        predecessor = [None] * self.V

        print(self.edges)
        # Step 2: Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    predecessor[v] = u  # Track the predecessor

        # Step 3: Check for negative weight cycles
        for u, v, w in self.edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return -1

        # Print the final distances from the source
        self.print_solution(dist, predecessor, source)
        return (dist, predecessor)

    def print_solution(self, dist, predecessor, source):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

        # Print paths from the source to each vertex
        print("\nShortest Paths from Source:")
        for i in range(self.V):
            if i != source and dist[i] != float("Inf"):
                path = self.get_path(predecessor, i)
                print(f"Shortest path to vertex {i}: {path} with total distance {dist[i]}")

    # Helper function to reconstruct the shortest path
    def get_path(self, predecessor, vertex):
        path = []
        current = vertex
        while current is not None:
            path.insert(0, current)  # Insert the node at the beginning of the list
            current = predecessor[current]  # Move to the predecessor node

        return path

    def construct_path(self, path, source, destination):
        if len(path) == 0:
            return "No Path"

        if path[0] != source or path[-1] != destination:
            return "No Path Detected"

        return ' -> '.join(map(str, path))

# Example graph based on the provided edges:
# g = Graph(3)  # Three vertices (A -> 0, B -> 1, C -> 2)
# g.add_edge(0, 1, 4)  # A -> B, weight 4
# g.add_edge(0, 2, 5)  # A -> C, weight 5
# g.add_edge(1, 2, -3)  # B -> C, weight -3

# Run the Bellman-Ford algorithm starting from vertex 0 (A)
# g.bellman_ford(0)
