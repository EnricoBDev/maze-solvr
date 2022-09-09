from collections import deque
from PIL import Image

from img_manipulation import draw_alg_frame, resize_Image

def solve(maze, adj_list):
    start = maze.start
    end = maze.end

    queue = deque([start])
    visited = [False] * (maze.width * maze.height)
    prev = [None] * (maze.width * maze.height)

    visited[start.coords[0] * maze.width + start.coords[1]] = True

    frame = Image.new(mode = "RGBA", size = (maze.width, maze.height), color = (0, 0, 0, 0))
    frames = []

    while queue:
        current = queue.pop()

        if current.__repr__() == end.__repr__():
            break
        
        for i in adj_list.get(current.__repr__()):
            visited_pos = i.coords[0] * maze.width + i.coords[1]
            if visited[visited_pos] == False:    
                frame = draw_alg_frame(frame, current, i)
                queue.appendleft(i)
                visited[visited_pos] = True
                prev[visited_pos] = current
        
        frames.append(frame.convert("RGBA"))

    path = deque()
    current = end
    while current != None:
        path.appendleft(current)
        current = prev[current.coords[0] * maze.width + current.coords[1]]
    
    if len(path) > 1:
        return path, frames
    else: 
        return False