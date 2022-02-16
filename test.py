import os

class Lines():
    def __init__(self, xo_list, size=17):
        self.xo_list = xo_list
        self.size = size
        self.index = -1
        self.lines = []
        self.x = \
            [
                "\\      /",
                "  \\  /  ",
                "   \\/   ",
                "   /\\   ",
                "  /  \\  ",
                "/      \\"
            ]
        self.o =\
            [
                "  ----  ",
                " /    \\",
                "|      |",
                "|      |",
                " \\    /",
                "  ----  "
            ]
        self._set_lines()

    def _set_lines(self):
        line = self.get_clean_line()
        for l in range(6):
            for i in range(3):
                xo = self.xo_list[i]
                if xo:
                    self._add_xo(xo, line, (i, l))
            self.lines.append(line)

    def _add_xo(self, xo, line, idx):
        start = idx[0]*self.size + 1
        xo = self.x if xo == "x" else self.o
        line[start : start + len(xo)] = xo[idx[1]]
    
    def set_xo_list(self, xo_list:list):
        self.xo_list = xo_list

    def get_clean_line(self):
        cube = "|" + " " * self.size
        line = cube * 3 + "|"
        return line
        
    def get_split_line(self):
        line = "+" + "-" * self.size
        return line * 3 + "+"

    def get_line(self):
        self.index += 1
        line = self.lines[self.index]
        return line


def print_board(size:int, xo_list:list, lines:Lines):
    split_line = lines.get_split_line()
    clean_line = lines.get_clean_line()
    print(split_line)
    for i in range(3):
        print(clean_line)
        for i in range(6):
            print(lines.get_line())
        print(clean_line)
        print(split_line)


def check_move(i:int, xo_list:list):
    pass


def game():
    xo_list = ["" for i in range(9)]
    lines = Lines(xo_list, 17)
    finish = False
    counter = 0
    print_board(17, xo_list, lines)
    while not finish:
        x, y = input("Enter row and column to add a move: ")
        if 0 < x < 4 and 0 < x < 4:
            xo_list[x * y] = "x" if counter % 2 else "o"
            lines.set_xo_list(xo_list)
            check_move(x*y, xo_list)
            os.system("cls")
            print_board(17, xo_list, lines)
            counter += 1
        else:
            continue

if __name__ == "__main__":
    game()