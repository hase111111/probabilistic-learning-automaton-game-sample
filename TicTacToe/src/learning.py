"""learning.py"""

import tictactoe.data


def main():
    gene = tictactoe.data.BoardEnumerator()
    boards = gene.get_all_boards()
    print(len(boards))


if __name__ == "__main__":
    main()
