def solve1(file):
    with open(file, "r") as f:
        txt = f.read()
        if txt[-1] == "\n":
            txt = txt[:-1]
        ret = txt.split("+")
        return ret
def print1(ret):
    for txt in ret:
        print(txt)

print1(solve1("txt1.txt"))