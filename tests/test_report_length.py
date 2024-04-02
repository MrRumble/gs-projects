from lib.report_length import *

def test_str_in_report_length():
    result = report_length("John")
    assert result == 'This string was 4 characters long.'

def test_string_length_6_reported_correctly():
    result = report_length("Gerald")
    assert result == 'This string was 6 characters long.'

def test_str_length_empty():
    result = report_length("")
    assert result == 'This string was 0 characters long.'