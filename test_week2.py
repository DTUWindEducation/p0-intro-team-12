"""Test your functions from Week 2 assignment.
"""
import preclass_assignment.functions as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    text_exp = 'Hello, world!\n'
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == text_exp  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    size = 139
    text_exp = "Too small!\n"
    # when
    fxn.goldilock(size)
    captured = capsys.readouterr()
    # then
    assert captured.out == text_exp


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    max = 30
    exp_out = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    # when
    out = fxn.fibonacci_stop(max)
    # then
    assert exp_out == out


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    x = [-1, 2, 6, 95]
    status = [1, 0, 0, 0]
    exp_out = [-999, 2, 6, 95]
    # when
    out = fxn.clean_pitch(x, status)
    # then
    assert exp_out == out
