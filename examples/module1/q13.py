"""Module 1 Question 13: Write a Python program to solve the 8-puzzle using Breadth-First Search (BFS) and display the sequence of moves."""

from collections import deque
def bfs(start, goal):
    queue = deque([(start, [start])]); visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == goal: return path
        z = state.index(0); r, c = divmod(z, 3)
        options = ([z-3] if r>0 else []) + ([z+3] if r<2 else []) + ([z-1] if c>0 else []) + ([z+1] if c<2 else [])
        for pos in options:
            nxt = list(state); nxt[z], nxt[pos] = nxt[pos], nxt[z]; nxt = tuple(nxt)
            if nxt not in visited:
                visited.add(nxt); queue.append((nxt, path+[nxt]))
    return None
start=(1,2,3,4,0,6,7,5,8); goal=(1,2,3,4,5,6,7,8,0)
path=bfs(start, goal)
if path:
    for step,state in enumerate(path):
        print("Step",step)
        for i in range(0,9,3): print(state[i:i+3])
else: print("No solution found")
