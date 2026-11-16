import argparse


def main():
    parser = argparse.ArgumentParser(
        description="cli2playbook CLI"
    )
    
    # the -i is used to indicate the interactive mode
    parser.add_argument(
        "-i",
        action="store_true",
        help="Run in interactive mode"
    )
    
    # Optional positional argument for the command string
    parser.add_argument(
        "command",
        nargs="?",
        type=str,
        help="Docker/Podman command string"
    )

    args = parser.parse_args()

    # Check if -i was passed
    if args.i:
        print("=========================\nStarting Interactive mode\n=========================\n")
    else:
        print(f"============\nDirect mode\n============\n")


if __name__ == "__main__":
    main()
