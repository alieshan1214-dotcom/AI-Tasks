# Import the heapq module to use for our priority queue (open list)
import heapq

# Define the heuristic values for each node in the graph
heuristics = {
    # Node S has a heuristic value of 10
    'S': 10,
    # Node A has a heuristic value of 8
    'A': 8,
    # Node B has a heuristic value of 6
    'B': 6,
    # Node C has a heuristic value of 4
    'C': 4,
    # Node D has a heuristic value of 3
    'D': 3,
    # Node E has a heuristic value of 5
    'E': 5,
    # Node G has a heuristic value of 0 (goal node)
    'G': 0
}

# Define the graph as an adjacency list where each key is a node and the value is a list of tuples (neighbor, edge_weight)
graph = {
    # Node S connects to A with weight 2 and B with weight 5
    'S': [('A', 2), ('B', 5)],
    # Node A connects to C with weight 2 and D with weight 4
    'A': [('C', 2), ('D', 4)],
    # Node B connects to D with weight 5 and E with weight 1
    'B': [('D', 5), ('E', 1)],
    # Node C connects to G with weight 3
    'C': [('G', 3)],
    # Node D connects to G with weight 2
    'D': [('G', 2)],
    # Node E connects to G with weight 6
    'E': [('G', 6)],
    # Node G has no outgoing edges as it is the goal
    'G': []
}

# Define the A* search function that takes the graph, heuristics, start node, and goal node as parameters
def a_star_search(graph, heuristics, start, goal):
    # Initialize the open list as an empty list to store nodes to be explored
    open_list = []
    
    # Push the start node into the open list with its initial f-score (which is just the heuristic of start, since g=0)
    # The tuple format used is: (f_score, g_score, current_node, path_taken_so_far)
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))
    
    # Initialize a dictionary to keep track of the minimum g-score (actual cost) to reach each node
    g_scores = {start: 0}
    
    # Start a while loop that continues to run as long as there are nodes in the open list
    while open_list:
        # Pop the node with the lowest f-score from the priority queue (open list)
        current_f, current_g, current_node, current_path = heapq.heappop(open_list)
        
        # Check if the current node we just popped is the goal node we are looking for
        if current_node == goal:
            # If it is the goal, return the path taken to get here and the total actual cost (g-score)
            return current_path, current_g
            
        # Iterate over all the neighboring nodes of the current node in the graph
        for neighbor, weight in graph[current_node]:
            # Calculate the tentative g-score to reach this neighbor from the current node by adding the edge weight
            tentative_g = current_g + weight
            
            # Check if this neighbor has not been visited yet, or if we found a strictly cheaper path to it
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                # Update the g-score for this neighbor with the newly found cheaper cost
                g_scores[neighbor] = tentative_g
                
                # Calculate the f-score for this neighbor using the A* formula: f(n) = g(n) + h(n)
                f_score = tentative_g + heuristics[neighbor]
                
                # Create a new path list by appending the neighbor to the current path
                new_path = current_path + [neighbor]
                
                # Push the neighbor into the open list to explore it in future iterations
                heapq.heappush(open_list, (f_score, tentative_g, neighbor, new_path))
                
    # If the open list becomes empty and we haven't returned, the goal is unreachable from the start node
    return None, float('inf')

# Check if this Python script is being run directly as the main program
if __name__ == "__main__":
    # Define the starting node for our search
    start_node = 'S'
    # Define the goal node we want to reach
    goal_node = 'G'
    
    # Call the A* search function and unpack the returned path and cost into variables
    path, cost = a_star_search(graph, heuristics, start_node, goal_node)
    
    # Check if a valid path was successfully found
    if path:
        # Print the optimal path found by the algorithm, joined by arrows for readability
        print(f"Optimal Path found: {' -> '.join(path)}")
        # Print the total actual cost of the optimal path
        print(f"Total Cost: {cost}")
    # If no path was found (path is None)
    else:
        # Print a message stating the goal was not reachable
        print("Goal is not reachable from the start node.")
