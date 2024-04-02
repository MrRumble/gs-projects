from lib.present import *
import pytest


def test_wrap_single_present():
    present = Present()
    present.wrap("Cake")
    assert present.contents == 'Cake'

def test_unwrap_single_present():
    present = Present()
    present.wrap('Cake')
    present.unwrap()
    result= present.contents
    assert result == 'Cake'   

def test_present_already_wrapepd():
    present = Present()
    present.wrap('Cake')
    with pytest.raises(Exception) as e:
        present.wrap('Cake')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_no_presents_to_unwrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
