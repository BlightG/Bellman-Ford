class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []    # List to store graph edges
        self.predecessor = [[]] # list of predecessors for a destination
        self.dist = [[]] # a list of each iteration of a path
        self.path = []
        self.source = None

    # Function to add an edge
    def add_edge(self, u, v, weight):
        self.edges.append([u, v, weight])

    # Bellman-Ford algorithm to find the shortest path from the source
    def bellman_ford(self, source):
        # Step 1: Initialize distances from the source to all other vertices as infinity and source to 0
        dist = [[float("Inf")] * self.V for _ in range(self.V + 1)]
        dist[0][source] = 0
        predecessor = [[None] * self.V for _ in range(self.V + 1)]
        self.source = source

        # Step 2: Relax all edges |V| - 1 times
        for k in range(1, self.V + 1):
            # Step 3: Copy the values of the previous iteration
            dist[k] = dist[k - 1][:]
            predecessor[k] = predecessor[k - 1][:]
            for u, v, w in self.edges:
                if dist[k - 1][u] != float("Inf") and dist[k - 1][u] + w < dist[k][v]:
                    dist[k][v] = dist[k - 1][u] + w
                    predecessor[k][v] = u  # Track the predecessor
            if dist[k -1] == dist[k]:
                L = k - len(dist)
                dist[L:] = [dist[k-1] for _ in range(len(dist[L:]))]
                predecessor[L:] = [predecessor[k-1] for _ in range(len(predecessor[L:]))]
                break

        # Step 4: Check for negative weight cycles
        for u, v, w in self.edges:
            if dist[-1][u] != float("Inf") and dist[-1][u] + w < dist[-1][v]:
                return -1

        self.dist = dist
        self.predecessor = predecessor
        return dist

    # Helper function to reconstruct the shortest path
    def get_path(self, vertex, max_stops):
        path = []
        print(self.predecessor)
        current = vertex
        while current is not None:
            path.insert(0, current)  # Insert the node at the beginning of the list
            current = self.predecessor[max_stops][current]  # Move to the predecessor node

        self.path = path
        print(path)

    def construct_path(self, destination):
        if len(self.path) == 0:
            return -1

        if self.path[0] != self.source or self.path[-1] != destination:
            return -1

        return ' -> '.join(map(str, self.path))
