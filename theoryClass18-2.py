"""
Docstring for students_results_cli
This is an application for calculatingand storing student results.
This will run in the CLI.
If possible we will also save it in a .csv file.
"""

def print_menu() -> None:
    print("---------- Student Result Calculator ----------")
    print("1) Add student result + calculate results")


def main() ->None:
    print_menu()

if __name__ == "__main__":
    main()