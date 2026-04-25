
from collections import deque

# Graph of cities
graph = {

    "Islamabad": ["Rawalpindi", "Lahore", "Peshawar"],

    "Rawalpindi": ["Islamabad", "Peshawar", "Quetta"],

    "Peshawar": ["Islamabad", "Rawalpindi", "Quetta"],

    "Lahore": ["Islamabad", "Multan", "Quetta"],

    "Multan": ["Lahore", "Karachi", "Quetta"],

    "Quetta": ["Rawalpindi", "Peshawar", "Multan", "Karachi"],

    "Karachi": ["Multan", "Quetta"]

}


def bfs_shortest_path(graph, start, goal):

    visited = set()

    queue = deque([[start]])

    while queue:

        path = queue.popleft()

        node = path[-1]

        if node == goal:
            return path

        if node not in visited:

            visited.add(node)

            for neighbor in graph[node]:

                new_path = list(path)
                new_path.append(neighbor)

                queue.append(new_path)

    return None



start_city = "Islamabad"
goal_city = "Karachi"

shortest_path = bfs_shortest_path(graph, start_city, goal_city)

print("Shortest Path from Islamabad to Karachi:")
print(" → ".join(shortest_path))