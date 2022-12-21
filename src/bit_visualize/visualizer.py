"""Script to parse the command line and start a new session to
   visualize bit operations."""
from variables import GlobalVars, parse_comm


def main(args):
    """Instantiate global variables and start parsing the command line."""
    if args.bits not in (32, 64):
        print("Invalid bit count: must be either 32 or 64")
        return
    stored_vars = GlobalVars(args)

    while True:
        command = input(">> ")
        if parse_comm(command, stored_vars) < 0:
            break


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="init line")
    parser.add_argument("-b", "--bits", type=int, help="# of bits, 32 or 64")
    parser.add_argument("-s", action="store_true", help="signed bit")
    parser.add_argument(
        "-r", "--rest", type=float, default=0.2, help="Time to wait "
    )  # noqa: E501
    parser.add_argument(
        "-l", "--line", action="store_true", help="\n instead of \r"
    )  # noqa: E501

    arguments = parser.parse_args()
    main(arguments)
