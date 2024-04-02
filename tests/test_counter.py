from lib.counter import *

def test_counter_adds_11_to_1():
    counter = Counter()
    counter.add(11)
    result = counter.report()
    assert result == "Counted to 11 so far."     

def test_counter_works_twice():
    counter = Counter()
    counter.add(11)
    counter.add(11)
    assert counter.count == 22

def test_counter_adds_0():
    counter = Counter()
    counter.add(0)
    result = counter.report()
    assert "Counter to 0 so far."
