""" Tests bit visualizer functions."""
from variables import GlobalVars, parse_comm


class PseudoArg:  # pylint: disable=R0903
    """Substitue argument parser for testing purposes."""

    def __init__(self, rest, line, bits, signed):
        self.rest = rest
        self.line = line
        self.bits = bits
        self.signed = signed


def test_dictionary_one():
    """Make sure variables are correctly inputted to dictionary."""
    args = PseudoArg(0.2, "\r", 32, 0)
    globs = GlobalVars(args)
    command = "var x = b110101"
    parse_comm(command, globs)

    assert (
        globs.search("x")
        == "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 1"
    )


def test_dictionary_two():
    """Make sure variables are correctly inputted to dictionary,
    when inputted as a binary string."""
    args = PseudoArg(0, "\r", 64, 0)
    globs = GlobalVars(args)
    command = "var x = b110101"
    parse_comm(command, globs)
    assert (
        globs.search("x")
        == "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 1"  # noqa: E501 # pylint: disable=C0301
    )


def test_left_shift():
    """Test left shift."""
    args = PseudoArg(0.2, "\r", 32, 0)
    globs = GlobalVars(args)
    command = "var x = 32"
    parse_comm(command, globs)

    command = "x = x << 2"
    parse_comm(command, globs)
    assert globs.string_to_val(globs.search("x")) == 128


def test_not():
    """Test the not (~x) function."""
    args = PseudoArg(0.2, "\r", 32, 0)
    globs = GlobalVars(args)
    command = "var x = 0"
    parse_comm(command, globs)

    command = "x = ~x"
    parse_comm(command, globs)
    assert (
        globs.search("x")
        == "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"
    )


def test_right_shift():
    """Test arithmetic right shift."""
    args = PseudoArg(0.2, "\r", 32, 0)
    globs = GlobalVars(args)
    command = "var x = 0"
    parse_comm(command, globs)

    command = "x = ~x"
    parse_comm(command, globs)
    compare = globs.search("x")

    command = "x = x >> 2"
    parse_comm(command, globs)

    assert globs.search("x") == compare


def test_right_shift_logical():
    """Test logical right shift function."""
    args = PseudoArg(0.2, "\r", 32, 0)
    globs = GlobalVars(args)
    command = "var x = 0"
    parse_comm(command, globs)

    command = "x = ~x"
    parse_comm(command, globs)
    compare = globs.search("x")

    command = "x = x >> 2 L"
    parse_comm(command, globs)

    assert globs.string_to_val(globs.search("x")) == globs.string_to_val(
        compare
    ) & (  # noqa: E501
        ~(1 << 31)
    ) & (
        ~(1 << 30)
    )


def test_conversion():
    """Test conversion from val to string and then back to val."""
    args = PseudoArg(0.2, "\n", 32, 0)
    globs = GlobalVars(args)
    command = "var x = 37"
    parse_comm(command, globs)

    assert 37 == globs.string_to_val(globs.search("x"))


# test bang operation


def test_bang():
    """Test !x operator."""
    args = PseudoArg(0.2, "\r", 32, 0)
    globs = GlobalVars(args)
    command = "var x = 37"
    parse_comm(command, globs)

    command = "var y = b0"
    parse_comm(command, globs)

    command = "x = !x"
    parse_comm(command, globs)

    command = "y = !y"
    parse_comm(command, globs)

    assert globs.string_to_val(globs.search("x")) == 0
    assert globs.string_to_val(globs.search("y")) == 1


def test_variable_assignment():
    """Make sure desired variable is correctly updated."""
    args = PseudoArg(0.2, "\r", 32, 0)
    globs = GlobalVars(args)
    command = "var x = 37"
    parse_comm(command, globs)

    command = "var y = b0"
    parse_comm(command, globs)

    command = "x = !y"
    parse_comm(command, globs)

    command = "y = !x"
    parse_comm(command, globs)

    assert globs.string_to_val(globs.search("y")) == 0
    assert globs.string_to_val(globs.search("x")) == 1
