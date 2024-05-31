def DFS(graph, start):
    # Initialize the visited set and the stack with the start node
    visited, stack = set(), [start]

    # While there are nodes in the stack
    while stack:
        # Pop a node from the stack
        vertex = stack.pop()

        # If the node has not been visited before
        if vertex not in visited:
            # Mark the node as visited
            visited.add(vertex)
            # Add the neighbors of the node to the stack
            stack.extend(set(graph[vertex].keys()) - visited)

    # Return the visited nodes
    return visited
