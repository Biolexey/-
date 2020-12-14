dic = {"1": 0, "2": 1, "3": 2, "A": 0, "B": 1, "C": 2}

def is_same(txt):
    ret = True
    s = txt[0]
    for mark in txt:
        if mark != s:
            ret = False
            break
    return ret 

def is_same_as_mark(txt, m):
    ret = True
    for mark in txt:
        if mark != m:
            ret = False
            break
    return ret

def get_revmark(mark):
    if mark == "O":
        return "X"
    elif mark == "X":
        return "O"
    else:
        return "-"

def has2(txt, mark):
    tmp = 0
    revm = get_revmark(mark)
    for m in txt:
        if m == revm:
            return False
        elif m == mark:
            tmp += 1
    return tmp >= 2

def diff2(txt):
    return ("O" in txt) and ("X" in txt)

def who_win(game):
    dic = {}
    dic['row1'] = game[0][0] + game[0][1] + game[0][2]
    dic['row2'] = game[1][0] + game[1][1] + game[1][2]
    dic['row3'] = game[2][0] + game[2][1] + game[2][2]
    dic['col1'] = game[0][0] + game[1][0] + game[2][0]
    dic['col2'] = game[0][1] + game[1][1] + game[2][1]
    dic['col3'] = game[0][2] + game[1][2] + game[2][2]
    dic['cross1'] = game[0][0] + game[1][1] + game[2][2]
    dic['cross2'] = game[0][2] + game[1][1] + game[2][0]
    for txt in dic.values():
        if is_same(txt):
            return txt[0]
    return "-"

class Board(object):
    def __init__(self, game):
        self.game = game
        self.O_num = 0
        self.X_num = 0

        for row in game:
            for mark in row:
                if mark == "O":
                    self.O_num += 1
                elif mark == "X":
                    self.X_num += 1

        if self.O_num == self.X_num:
            self.next_turn = "O"
        else:
            self.next_turn = "X"

        self.game_turn = self.O_num + self.X_num

        if self.game_turn >= 9:
            self.is_game_end = True
        else:
            self.is_game_end = False
    
    def __repr__(self):
        ret = ""
        for row in self.game:
            ret += ("".join(row) + "\n")
        return ret

    def put(self, inp):
        if self.game_turn >= 9:
            return "すでにゲームは終了しています"
        
        i = dic[inp[0]]
        j = dic[inp[1]]
        if self.game[i][j] != "-":
            return "すでに埋まっています"
        else:
            self.game[i][j] = self.next_turn
            if self.next_turn == "O":
                self.next_turn = "X"
            else:
                self.next_turn = "O"
        
        self.game_turn += 1
        win = who_win(self.game)
        if win != "-":
            self.is_game_end = True
            return "{0}が勝ちました\n{1}".format(win, self)
        elif self.game_turn >= 9:
            self.is_game_end = True
            return "引き分けです\n{0}".format(self)
        else:
            return str(self)

def inputdata(file):
    with open(file, "r", encoding="ascii") as f:
        txt = f.readlines()
        game = [["-" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                game[i][j] = txt[i][j]
        return Board(game)

def solve1():
    for i in range(1, 5):
        board = inputdata("test00{0}.txt".format(i))
        print(board)

