import shutil


def center(text: str) -> None:
    """center_text - Center the provided text in the terminal.

    Extended Summary:
    This function takes a multi-line string as input and centers each line
    within the current terminal width. It calculates the necessary padding
    for each line to be centrally aligned and prints it accordingly.

    Arguments:
        text {str} -- The text to be centered, which can span multiple lines.
    """

    lines = text.split('\n')
    terminal_width, _ = shutil.get_terminal_size()

    for a in lines:
        padding = (terminal_width - len(a)) // 2
        print(" " * padding + a)


def alignment(text1: str, text2: str) -> None:
    """alignment - Align left and right text with in the terminal.

    Extended Summary:
    This function prints two strings on the same line in the terminal,
    one aligned to the left and the other to the right. It splits the input
    strings into lines and calculates the necessary padding between the
    left and right text to ensure proper alignment within the terminal width.

    Arguments:
        text1 {str} -- The text to be aligned on the left.
        text2 {str} -- The text to be aligned on the right.
    """

    lines1 = text1.split('\n')
    lines2 = text2.split('\n')
    terminal_width, _ = shutil.get_terminal_size()

    for index, b in enumerate(lines1):
        padding = (terminal_width - len(lines2[index]) - len(b))
        print(b + " " * padding + lines2[index])
