# Graph

## Definition

"Graph" is a non-linear data structure consisting of vertices and edges. The terminologies of graph are presented below:
- vertex: nodes inside a graph
- edge: the connection between two vertices
- path: the sequence of vertices to go through from one vertex to another. For example, [`node A`, `node B`, `node C`] can be a 
path from `A` to `C`, where `A`, `B`, `C` are vertices of the graph.
- path length: the number of edges in a path.
- cycle: a path where the starting point and endpoint are the same vertex.
- negative weight cycle: in a “weighted graph”, if the sum of the weights of all edges of a cycle is a negative value, it is a negative weight cycle.
- connectivity: if there exists at least one path between two vertices, these two vertices are connected
- degree of a vertex: the term "degree" applies to unweighted graphs. The degree of a vertex is the number of 
edges connecting the vertex.
- in-degree: "in-degree" is a concept in directed graphs. If the in-degree of a vertex is d, there are d directional
edges incident to the vertex.
- out-degree: "in-degree" is a concept in directed graphs. If the in-degree of a vertex is d, there are d directional
edges incident from the vertex.


## Category

Graphs are categorized to three types: undirected graphs, directed graphs, and weighted graphs.

#### Undirected Graphs:
The edges between any two vertices in an "undirected graph" do not have a direction, indicating a two-way relationship.

#### Directed Graphs:
The edges between any two vertices in a "directed graph" are directional.

#### Weighted Graphs:
The edges between any two vertices has an associated weight, which can be any metric (e.g. time, distance, size, etc.).

