import heapq

def uniform_cost_search(graph, start, goal):
    # Initialize the queue with the start node and cost 0
    queue = [(0, start, [])]
    # Initialize an empty set for seen nodes
    seen = set()

    # While there are nodes in the queue
    while queue:
        # Pop the node with the smallest cost
        (cost, node, path) = heapq.heappop(queue)

        # If the node has not been seen before
        if node not in seen:
            # Add the node to the path
            path = path + [node]
            # Mark the node as seen
            seen.add(node)

            # If the node is the goal
            if node == goal:
                # Return the cost and path
                return cost, path

            # For each neighbor of the current node
            for next_node, edge_cost in graph[node].items():
                # If the neighbor has not been seen before
                if next_node not in seen:
                    # Add the neighbor to the queue with the cost and path
                    heapq.heappush(queue, (cost + edge_cost, next_node, path))

    # If no path is found, return infinity and an empty path
    return float('inf'), []
