import sys
from pathlib import Path

from colorama import Fore, Style, init

init()


def print_directory_tree(directory: Path, indent: str = "") -> None:
    """
    Recursively print the directory tree, using different colors for directories and files.

    :param directory: The Path object of the directory to traverse.
    :param indent: The indentation string used for nested directories (default is empty string).
    """
    for item in sorted(
        directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower())
    ):
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
            print_directory_tree(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def visualize_directory(path_str: str) -> None:
    """
    Visualize the structure of the directory at the given path with colored output.

    :param path_str: The path to the directory as a string.
    """
    path = Path(path_str)
    if not path.exists():
        print(f"Error: The path '{path_str}' does not exist.")
        return
    if not path.is_dir():
        print(f"Error: The path '{path_str}' is not a directory.")
        return
    print_directory_tree(path)
