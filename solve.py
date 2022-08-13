from collections import deque

def solve(maze, adj_list):
    start = maze.start
    end = maze.end

    queue = deque([start])
    visited = [False] * (maze.width * maze.height)
    prev = [None] * (maze.width * maze.height)

    visited[start.coords[0] * maze.width + start.coords[1]] = True

    while queue:
        current = queue.pop()

        if current == end:
            break
        
        for i in adj_list.get(current.__repr__()):
            visited_pos = i.coords[0] * maze.width + i.coords[1]
            if visited[visited_pos] == False:
                queue.appendleft(i)
                visited[visited_pos] = True
                prev[visited_pos] = current

    path = deque()
    current = end
    while current != None:
        path.appendleft(current)
        current = prev[current.coords[0] * maze.width + current.coords[1]]
    
    if len(path) > 1:
        return path
    else: 
        return False