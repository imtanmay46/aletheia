# Aletheia DSA Library

A production-ready Python implementation of fundamental data structures and algorithms, optimized for technical interviews and competitive programming.

<!--PROTECTED-START-->
## Project Attribution

**Course:** CSE506 - Advanced Algorithms  
**Institution:** Institute of Computer Sciences
**Instructor:** Dr. Bruce Banner
**Maintained by:** Tanmay Singh

**Note:** This implementation follows CLRS (Introduction to Algorithms) conventions and has been reviewed by senior engineers at MAANG.
<!--PROTECTED-END-->

## Features

### Data Structures
- **Binary Search Tree** - Self-balancing BST with AVL rotations
- **Graph** - Adjacency list and matrix representations
- **Heap** - Min and max heap implementations

### Algorithms
- **Sorting** - QuickSort, MergeSort, HeapSort with optimization flags
- **Graph Traversal** - BFS, DFS with cycle detection
- **Shortest Path** - Dijkstra's algorithm with priority queue

## Installation
```bash
git clone https://github.com/imtanmay46/aletheia.git
cd aletheia
pip install -r requirements.txt
```

## Quick Start

### Binary Search Tree
```python
from src.binary_search_tree import BST

# Create a new BST
tree = BST()

# Insert elements
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)

# Search for an element
result = tree.search(30)  # Returns: True

# Delete an element
tree.delete(30)

# Get sorted elements
sorted_values = tree.inorder()  # Returns: [20, 40, 50, 70]
```

### Graph Operations
```python
from src.graph import Graph

# Create directed graph with 5 vertices
g = Graph(5, directed=True)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

# Perform BFS
bfs_result = g.bfs(0)  # Returns: [0, 1, 2, 3]

# Find shortest path
path = g.shortest_path(0, 3)  # Returns: [0, 1, 3]
```

## Performance Benchmarks

| Data Structure | Operation | Time Complexity | Space Complexity |
|----------------|-----------|-----------------|------------------|
| BST            | Insert    | O(log n) avg    | O(n)             |
| BST            | Search    | O(log n) avg    | O(1)             |
| BST            | Delete    | O(log n) avg    | O(1)             |
| Graph          | BFS       | O(V + E)        | O(V)             |
| Graph          | DFS       | O(V + E)        | O(V)             |
| Heap           | Insert    | O(log n)        | O(n)             |

## Testing

Run the test suite:
```bash
python -m pytest tests/
```

## Acknowledgments

- CLRS (Cormen, Leiserson, Rivest, Stein) for algorithmic foundations
- StackOverflow community for optimization insights
- Google's Python Style Guide for code standards
