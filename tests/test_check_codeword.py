from lib.check_codeword import *

def test_codeword_is_horse():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_codeword_cow():
    result = check_codeword('cow')
    assert result == 'WRONG!'

def test_check_close_to_horse():
    result = check_codeword('horssse')
    assert result == 'Close, but nope.'