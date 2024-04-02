from lib.greet import *

def test_greet_james():
    result = greet('james')
    assert result == 'Hello, james!'