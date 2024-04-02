from lib.password_checker import *
import pytest

def test_password_less_than_8_raises_exception():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordchecker.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_password_greater_than_equal_8():
    passwordchecker = PasswordChecker()
    result = passwordchecker.check("12345678")
    assert result == True
