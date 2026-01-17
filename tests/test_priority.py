from src.triage import calculate_priority

def test_priority_p1():
    assert calculate_priority(1, 1) == "P1"

def test_priority_p2():
    assert calculate_priority(1, 2) == "P2"

def test_priority_p4():
    assert calculate_priority(3, 3) == "P4"
