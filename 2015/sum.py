def solve1(file):
    with open(file, "r") as f:
        txt = f.read()
        print(txt.count(";"))
solve1("txt1.txt")

def solve2(file):
    with open(file, "r") as f:
        txt = f.readlines()
        for index, t in enumerate(txt):
            if "main" in t:
                print(f"{index+1}: {t[:-1]}")
solve2("txt2.txt")


