import pytest
from program import divide_numbers, reverse_string, get_list_element

def test_divide_numbers():
    assert divide_numbers(15, 0) == "undefined"
    assert divide_numbers(0, 15) == 0
    assert divide_numbers(15, 3) == 5
    assert divide_numbers(15, 14) == 1.07


def test_reverse_string():
    assert reverse_string("Hello") == "OLLEh"
    assert reverse_string(1) == "Not a string"


def test_get_list_element():
    test_list = ["a", "b", "c", "d"]
    assert get_list_element(test_list, 0) == "a"
    assert get_list_element(test_list, 1) == "b"
    assert get_list_element(test_list, 2) == "c"
    assert get_list_element(test_list, 3) == "d"
    assert get_list_element(test_list, 4) == IndexError
    assert get_list_element(test_list, -1) == IndexError