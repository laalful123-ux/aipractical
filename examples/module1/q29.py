"""Module 1 Question 29: Create a simple table-driven agent in Python. Define its percepts, actions and table, then test it with sample inputs."""

percepts=[("A","Dirty"),("A","Clean"),("B","Dirty"),("B","Clean")]
actions=["Suck","Right","Suck","Left"]; agent_table=dict(zip(percepts,actions))
print(agent_table)
for percept in percepts: print("Percept:",percept,"Action:",agent_table[percept])
