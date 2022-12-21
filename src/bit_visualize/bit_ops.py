"""Implementation of bit operations, such as x >> y
(arithmetic and logical), x << y, ~x , and !x."""

from time import sleep
import sys


def left_shift(bits, shift, globs):
    """Left shift operation, bits << shift."""
    print_initial(bits, globs)
    if shift.isnumeric():
        shift = int(shift)
    else:
        shift = globs.search(shift)
        shift = globs.string_to_val(shift)
    initial_bits = bits
    bits = globs.string_to_val(bits)
    bits = bits << shift
    string_bits = globs.val_to_string(bits)

    # need to print right to left
    if globs.bits == 32:
        length = 64
        empty_string = " " * 64
    else:
        length = 128
        empty_string = " " * 128
    if globs.line == "\r":
        empty_string = initial_bits
    empty_string = list(empty_string)
    for index, bit in enumerate(reversed(string_bits)):
        if length - 1 - index - 1 < 0:
            break
        empty_string[(length - 1) - index - 1] = bit
        sys.stdout.write("".join(empty_string) + "\r")
        sys.stdout.flush()
        sleep(globs.rest)
    print("\n")
    print(globs.string_to_val(string_bits))
    return string_bits


def right_shift(bits, shift, globs, logic=False):
    """Right shift operation, bits >> shift. If logic is true,
    then it becomes a logical right shift."""
    print_initial(bits, globs)
    if shift.isnumeric():
        shift = int(shift)
    else:
        shift = globs.search(shift)
        shift = globs.string_to_val(shift)

    bits = globs.string_to_val(bits)
    if not logic or (bits & 1 << (globs.bits - 1) == 0):
        # artithmetic shift or logic shift but MSB is 0 so doesn't matter
        bits = bits >> shift
        for times in range(1, shift + 1):
            bits |= (1 << globs.bits - 1) >> (times - 1)
        string_bits = globs.val_to_string(bits)
    else:
        # logic shift and MSB is 1
        bits = bits >> shift
        # this isn't actually necessary right now because
        # python is doing a logical shift naturall but it shouldn't
        bits &= ~((1 << globs.bits - 1) >> (shift - 1))
        string_bits = globs.val_to_string(bits)
    write_vector(string_bits, globs)
    print(globs.string_to_val(string_bits))
    return string_bits


def not_op(bits, globs):
    """Returns ~x."""
    print_initial(bits, globs)
    bits = bits.replace("1", "x")
    bits = bits.replace("0", "1")
    bits = bits.replace("x", "0")
    write_vector(bits, globs)
    print(globs.string_to_val(bits))
    return bits


def bang_op(bits, globs):
    """Returns !x."""
    print_initial(bits, globs)
    if "1" in bits:
        if globs.bits == 32:
            bits = "{0:032b}".format(0)  # pylint: disable=C0209
        else:
            bits = "{0:064b}".format(0)  # pylint: disable=C0209
    else:
        if globs.bits == 32:
            bits = "{0:032b}".format(1)  # pylint: disable=C0209
        else:
            bits = "{0:064b}".format(1)  # pylint: disable=C0209
    write_vector(bits, globs)
    print(globs.string_to_val(bits))
    return bits


def write_vector(bits, globs, rest=False):
    """Displays the final vector from left to right."""
    if not rest:
        rest = globs.rest
    else:
        rest = 0
    for char in bits:
        sleep(rest)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")


def print_initial(bits, globs):
    """Print the initial value of bits, called before operations."""
    sys.stdout.write(bits + globs.line)
    sys.stdout.flush()
    sleep(1)
