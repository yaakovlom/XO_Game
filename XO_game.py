import os
import time

class Lines():
    def __init__(self, xo_list, size=17):
        self.xo_list = xo_list
        self.size = size
        self.index = -1
        self.lines = []
        self.x = \
            [
                "  \\        /  ",
                "    \\    /    ",
                "      \\/      ",
                "      /\\      ",
                "    /    \\    ",
                "  /        \\  "
            ]
        self.o =\
            [
                "     ----     ",
                "    /    \\    ",
                "   |      |   ",
                "   |      |   ",
                "    \\    /    ",
                "     ----     "
            ]
        self._set_lines()

    def _set_lines(self):
        for l in range(6):
            line = self.get_base_line()
            for i in range(3):
                if not self.xo_list[i]:
                    xo = "              "
                elif self.xo_list[i] == "x":
                    xo = self.x[l]
                else:
                    xo = self.o[l]
                line = self._add_xo(xo, line, i)
            self.lines.append(line)

    def _add_xo(self, xo:str, line:str, idx:int):
        line = line.replace(str(idx) * self.size, xo)
        return line

    def get_base_line(self):
        cube = "|" + " "
        line = ""
        for i in range(3):
            _cube = cube.replace(" ", str(i) * self.size)
            line += _cube
        line += "|"
        return line

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


def print_board(xo_list:list):
    for i in range(3):
        lines = Lines(xo_list[i], 14)
        print(lines.get_split_line())
        for i in range(6):
            print(lines.get_line())
    print(lines.get_split_line())


def check_move(move:int, move_list:list):
    if len(move_list) == 3 and move_list[2] - move_list[1] > 2\
        and move_list[2] - move_list[1] == move_list[1] - move_list[0]: # lite check
        return move_list
    if move == 4: #  last move is in middle space
        for i in range(4):
            if i in move_list and 8 - i in move_list:
                return [i, move, 8 - i]
    else:
        if (move + 3) % 9 in move_list and (move - 3) % 9 in move_list: # check column
            return [(move + 3) % 9 for i in range(3)]
        else:
            row_center = move // 3 * 3 + 1
            if row_center - move and row_center in move_list and row_center * 2 - move in move_list: # check rows
                return [move, row_center, row_center * 2 - move]
            elif (not row_center - move) and move + 1 in move_list and move - 1 in move_list:
                return [move - 1, move, move + 1]
        if 4 in move_list and 8 - move in move_list: # check slash
                return [move, 4, 8 - move]
    return {}


def intro(xo_list):
    _xo_list = [\
        ["x", "o", "x"],
        ["o", "x", "o"],
        ["x", "o", "x"],
        ]
    for i in range(6):
        os.system("cls")
        print_board(_xo_list if i % 2 else xo_list)
        time.sleep(0.25)




def game(xo_list):
    finish = False
    counter = 0
    move_list = [[], []]
    while not finish:
        os.system("cls")
        print_board(xo_list)
        move = int(input("Enter number (1-9) for the next move: ")) - 1
        if 0 <= move < 9 and not xo_list[move // 3][move % 3]:
            player = counter % 2
            xo_list[move // 3][move % 3] = "x" if player else "o"
            move_list[player].append(move)
            move_list[player] = sorted(move_list[player])
            if counter >= 4:
                finish = check_move(move, move_list[player])
            if counter == 8:
                break
            counter += 1
    return finish, xo_list

def winner(win, xo_list):
    char = xo_list[win[0] // 3][win[0] % 3]
    for i in range(9):
        for xo in win:
            xo_list[xo // 3][xo % 3] = "" if i % 2 else char
        os.system("cls")
        print_board(xo_list)
        time.sleep(0.25)

def main():
    xo_list = [["", "", ""] for i in range(3)]
    intro(xo_list)
    win, xo_list = game(xo_list)
    if win:
        winner(win, xo_list)
    else:
        os.system("cls")
        print("\n\n\n\n\n\n")
        print("game over..".center(40))
        print("\n\n\n\n\n\n")

if __name__ == "__main__":
    main()
