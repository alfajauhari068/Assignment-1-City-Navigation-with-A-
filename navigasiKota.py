import heapq
import math

def heuristic(a, b, type='euclidean'):
    if type == 'euclidean':
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    else:
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star(graph, start, end, coords):
    open_heap = []
    heapq.heappush(open_heap, (0, start))
    came_from = {}
    g_score = {city: float('inf') for city in graph}
    g_score[start] = 0
    f_score = {city: float('inf') for city in graph}
    f_score[start] = heuristic(coords[start], coords[end])

    while open_heap:
        current = heapq.heappop(open_heap)[1]
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in graph[current]:
            tentative_g = g_score[current] + heuristic(coords[current], coords[neighbor])
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(coords[neighbor], coords[end])
                heapq.heappush(open_heap, (f_score[neighbor], neighbor))
    return []


kota = {"A": (0, 0), "B": (2, 1), "C": (4, 2), "D": (5, 5), "E": (1, 4)}
jalan = {"A": ["B", "E"], "B": ["A", "C"], "C": ["B", "D"], "D": ["C"], "E": ["A", "D"]}

path = a_star(jalan, "A", "D", kota)
print("Jalur terpendek:", path)
