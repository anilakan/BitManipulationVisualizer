"""Defines the Global Variables class, and some helper functions that work
   on variables that the user will be using."""
import bit_ops


def save_variable(command, stored_vars):
    """Save a variable into the global dictionary."""
    if not stored_vars.search(command[1]):
        stored_vars.add_var(command[1], command[3])


class GlobalVars:
    """Global variables class for attributes that need to be passed around between
    functions."""

    def __init__(self, args):
        """Initialize the object."""
        self.variables = {}
        self.rest = args.rest
        if args.line:
            self.line = "\n"
        else:
            self.line = "\r"
        self.bits = args.bits

    def add_var(self, var, bits):
        """Add a variable into the dictionary, saved in string form."""
        if "b" in bits:
            bits = bits.split("b")[1]
            bits = self.string_to_val(bits)
        string_form = self.val_to_string(bits)
        self.variables[var] = string_form

    def search(self, var):
        """Search defined variables that are already stored."""
        if self.variables.get(var):
            return self.variables[var]
        return None

    def update(self, var, new_bits):
        """Update an entry that already exists."""
        # error check?
        self.variables[var] = new_bits

    def val_to_string(self, val):
        """Convert an int to a string."""
        if self.bits == 32:
            string_form = "{0:032b}".format(int(val))  # pylint: disable=C0209
        else:
            string_form = "{0:064b}".format(int(val))  # pylint: disable=C0209
        string_form = string_form.replace("", " ")[1:-1]
        return string_form

    @staticmethod
    def string_to_val(bits):
        """Convert a string to an int."""
        bits = bits.replace(" ", "")
        # take in the sign here
        bits = int(bits, 2)
        return bits

    def print_vars(self, binary=False):
        """Print out the dictionary"""
        for item in self.variables.items():
            value = item[1]
            if binary:
                value = self.string_to_val(value)
            print(item[0] + ": " + str(value))


def parse_comm(command, stored_vars):
    """Parse the command line to find the desired operation."""
    command = command.split()
    op_code = command[0]
    if "var" == op_code:
        # can only create a new variable like this
        save_variable(command, stored_vars)
        return 0
    if "quit" == op_code:
        return -1
    if "display" == op_code:
        try:
            if command[1] == "b":
                stored_vars.print_vars(binary=True)
        except:  # noqa: E722 # pylint: disable=W0702
            stored_vars.print_vars()
        return 0

    action = command[2]
    if "~" in action or "!" in action:
        bits = stored_vars.search(action[1])
        if "~" in action:
            stored_vars.update(op_code, bit_ops.not_op(bits, stored_vars))
        elif "!" in action:
            stored_vars.update(op_code, bit_ops.bang_op(bits, stored_vars))
    else:
        bits = stored_vars.search(action[0])
        if ">>" in command:
            stored_vars.update(
                op_code,
                bit_ops.right_shift(
                    bits, command[4], stored_vars, logic=bool("L" in command)
                ),
            )
        elif "<<" in command:
            stored_vars.update(
                op_code, bit_ops.left_shift(bits, command[4], stored_vars)
            )
    return 0
