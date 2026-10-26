from aipractical.api import _DATA, _resolve
def test_question_counts():
    assert len([x for x in _DATA if x["module"]==1]) == 29
    assert len([x for x in _DATA if x["module"]==2]) == 34
def test_full_question_lookup():
    x=_resolve("Implement Breadth-First Search (BFS) in Python to find the shortest path in an 8-puzzle. Use the given initial and goal configurations.")
    assert x and x["number"]==3
