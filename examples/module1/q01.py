"""Module 1 Question 1: Define PEAS for a vacuum-cleaner agent. Classify its environment as fully/partially observable, deterministic/stochastic, and episodic/sequential. Implement a simple table-driven agent in Python."""

table = {("A","Dirty"): "Suck", ("A","Clean"): "Right", ("B","Dirty"): "Suck", ("B","Clean"): "Left"}
location = input("Enter location (A/B): ").strip().upper()
status = input("Enter status (Dirty/Clean): ").strip().title()
print("Action:", table.get((location, status), "No rule defined"))
