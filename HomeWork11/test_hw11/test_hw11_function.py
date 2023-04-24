import pytest

import HomeWork11.hw11


testcases_positive = [
    ("длоОЛО 55 ! ", "ОЛО"),
    ("!!!@#$%^&*()", ""),
    ("Hello, World!", "HW"),
    ("", "")
]

testcases_negative = [
    ("aBcDefghIjKlmnopqrsTuvWxyZ", "ABCDEFGHIJKLmnopqrstuvwx"),
    ("до тих пір, поки не знайдете свою силу", "Т")
]

testcases_error = [
    (1, TypeError),
    (1.1, TypeError),
    (None, TypeError),
    (True, TypeError),
    (set, TypeError),
]

@pytest.mark.parametrize('writen_string, expected', testcases_positive)
def test_positive_cases(writen_string, expected):
    assert HomeWork11.hw11.clean_string(writen_string) == expected, 'something went wrong'

@pytest.mark.parametrize('writen_string, unexpected', testcases_negative)
def test_negative_cases(writen_string, unexpected):
    assert HomeWork11.hw11.clean_string(writen_string) != unexpected

@pytest.mark.parametrize('writen_string, expected_error', testcases_error)
def test_error_cases(writen_string, expected_error):
    with pytest.raises(expected_error):
        HomeWork11.hw11.clean_string(writen_string)

