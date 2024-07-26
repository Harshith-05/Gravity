import numpy as np
import matplotlib.pyplot as plt
import heapq

# Define the A* algorithm
def astar(grid, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def reconstruct_path(came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, end), 0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current == end:
            return reconstruct_path(came_from, current)

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if (0 <= neighbor[0] < grid.shape[0] and
                0 <= neighbor[1] < grid.shape[1] and
                grid[neighbor] == 0):

                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], tentative_g_score, neighbor))

    return []


# Define the grid map
def create_grid_with_craters(size, craters):
    grid = np.zeros(size)
    for (x, y) in craters:
        grid[x, y] = 1
    return grid

# Visualize the grid and path
def visualize(grid, path):
    plt.imshow(grid, cmap='gray')
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, marker='o', color='r')
    plt.title('Pathfinding on Moon')
    plt.show()

# Example usage
size = (100, 100)  # Grid size
craters = [(20, 20), (25, 25), (30, 30), (40, 40)]  # Example crater coordinates
start = (10, 10)
end = (90, 90)

grid = create_grid_with_craters(size, craters)
path = astar(grid, start, end)
visualize(grid, path)
