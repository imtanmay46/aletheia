"""
Graph Implementation using Adjacency List
Supports both directed and undirected graphs.
"""

from collections import deque, defaultdict


class Graph:
    """Graph data structure with common algorithms."""
    
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_list = defaultdict(list)
    
    def add_edge(self, src, dest, weight=1):
        """Add an edge to the graph."""
        self.adj_list[src].append((dest, weight))
        if not self.directed:
            self.adj_list[dest].append((src, weight))
    
    def bfs(self, start):
        """Breadth-first search from start vertex."""
        visited = [False] * self.num_vertices
        queue = deque([start])
        visited[start] = True
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor, _ in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """Depth-first search from start vertex."""
        visited = [False] * self.num_vertices
        result = []
        self._dfs_helper(start, visited, result)
        return result
    
    def _dfs_helper(self, vertex, visited, result):
        visited[vertex] = True
        result.append(vertex)
        
        for neighbor, _ in self.adj_list[vertex]:
            if not visited[neighbor]:
                self._dfs_helper(neighbor, visited, result)
    
    def shortest_path(self, start, end):
        """Find shortest path using BFS (unweighted)."""
        if start == end:
            return [start]
        
        visited = [False] * self.num_vertices
        parent = [-1] * self.num_vertices
        queue = deque([start])
        visited[start] = True
        
        while queue:
            vertex = queue.popleft()
            
            for neighbor, _ in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = vertex
                    queue.append(neighbor)
                    
                    if neighbor == end:
                        return self._reconstruct_path(parent, start, end)
        
        return []  # No path found
    
    def _reconstruct_path(self, parent, start, end):
        path = []
        current = end
        while current != -1:
            path.append(current)
            if current == start:
                break
            current = parent[current]
        return path[::-1]
