import numpy as np
from collections import deque

# take the maze, start, goal, and length of one side as parameters
# marking visited nodes as 1 but could also just use a visited set and add the nodes as it traverses
def bfs(maze, start, goal, mlen):
    queue = deque([start])
    visited = np.zeros((mlen, mlen))
    while queue:

        x, y = queue.popleft()

        # if the goal is found, return true for now -> need to figure out what to do with display
        if(x, y) == goal:
            return True

        # if the node is blocked, on fire, or already visited, skip it and move on
        if maze[x, y] >= 1 or visited[x, y] == 1:
            continue

        # if the node is empty and hasnt been visited yet, add its neighbours to the queue with right/down prio
        elif maze[x, y] == 0 and visited[x, y] == 0:
            visited[x, y] = 1
            queue.append((x+1, y)) # add right
            queue.append((x, y+1)) # add down
            queue.append((x, y-1)) # add up
            queue.append((x-1, y)) # add left

    return True # filler for now
