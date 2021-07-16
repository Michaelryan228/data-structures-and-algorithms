import pytest

from brackets.brackets import validate_brackets

def test_initial_curly_brackets():
    actual = validate_brackets("{}")
    expected = True
    assert actual == expected

def test_case_two():
    actual = validate_brackets("{}(){}")
    expected = True
    assert actual == expected

def test_case_three():
    actual = validate_brackets("()[[Extra Characters]]")
    expected = True
    assert actual == expected

def test_case_four():
    actual = validate_brackets("(){}[[]]")
    expected = True
    assert actual == expected

def test_case_five():
    actual = validate_brackets("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected

def test_case_six():
    actual = validate_brackets("[({}]")
    expected = False
    assert actual == expected

def test_case_seven():
    actual = validate_brackets("(](")
    expected = False
    assert actual == expected

def test_case_eight():
    actual = validate_brackets("{(})")
    expected = False
    assert actual == expected

def test_case_nine():
    empty_arg = validate_brackets("")
    with pytest.raises(Exception) as exception_message:
        empty_arg.validate_brackets()
    assert str(exception_message.value) == "Empty string"

def test_case_ten():
    empty_arg = validate_brackets("daniel")
    with pytest.raises(Exception) as exception_message:
        empty_arg.validate_brackets()
    assert str(exception_message.value) == "Argument does not contain brackets"
