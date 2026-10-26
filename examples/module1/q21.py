"""Module 1 Question 21: Write a Python program to solve a water-jug problem using DFS; use jug capacities of your choice and reach a specified target amount."""

def dfs():
    stack=[(0,0)]; parent={(0,0):None}; visited=set(); goal=None
    while stack:
        a,b=stack.pop()
        if (a,b) in visited: continue
        visited.add((a,b))
        if a==2 or b==2: goal=(a,b); break
        x,y=min(a,3-b),min(b,4-a)
        for nxt in [(4,b),(a,3),(0,b),(a,0),(a-x,b+x),(a+y,b-y)]:
            if nxt not in parent: parent[nxt]=(a,b); stack.append(nxt)
    if goal is None: print("No solution"); return
    path=[]; cur=goal
    while cur is not None: path.append(cur); cur=parent[cur]
    print("State sequence (4L jug, 3L jug):")
    for state in reversed(path): print(state)
    print("Goal reached:",goal)
dfs()
