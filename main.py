import json

from strategy.dfs import DFS
from strategy.uniform import uniform_cost_search
from strategy.astar import A_star_search

with open('graphs.json', 'r') as input_file:
    graph = json.loads(input_file.read())

print("DFS:", DFS(graph, 'New York'))
print("Uniform Cost Search:", uniform_cost_search(graph, 'New York', 'Chicago'))
print("A* Search:", A_star_search(graph, 'New York', 'Chicago'))
