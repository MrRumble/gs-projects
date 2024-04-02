from lib.gratitudes import *

def test_one_added_gratitude():
    gratitude = Gratitudes()
    gratitude.add("I am in good health!")
    result = gratitude.format()
    assert result == "Be grateful for: I am in good health!"

def test_two_added_gratitiudes():
    gratitude = Gratitudes()
    gratitude.add("I am in good health!")
    gratitude.add("My class can add two gratitudes!")
    result = gratitude.format()
    assert result == "Be grateful for: I am in good health!, My class can add two gratitudes!"

def test_add_empty_gratitude():
    gratitude = Gratitudes()
    gratitude.add("I am in good health!")
    gratitude.add("")
    result = gratitude.format()
    assert result == "Be grateful for: I am in good health!"