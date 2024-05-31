import heapq
import math

locations = {
    'New York': (40.7128, 74.0060),
    'Los Angeles': (34.0522, 118.2437),
    'Chicago': (41.8781, 87.6298),
    'Houston': (29.7604, 95.3698),
    'Phoenix': (33.4484, 112.0740),
    'Philadelphia': (39.9526, 75.1652)
}

def heuristic(city1, city2):
    # Get the locations of the two cities
    loc1 = locations[city1]
    loc2 = locations[city2]

    # Calculate the difference in coordinates
    diff_lat = loc1[0] - loc2[0]
    diff_long = loc1[1] - loc2[1]

    # Calculate the straight-line distance using the Pythagorean theorem
    return math.sqrt(diff_lat ** 2 + diff_long ** 2)

def A_star_search(graph, start, goal):
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
                    # Add the neighbor to the queue with the cost, heuristic cost and path
                    heapq.heappush(queue, (cost + edge_cost + heuristic(next_node, goal), next_node, path))

    # If no path is found, return infinity and an empty path
    return float('inf'), []