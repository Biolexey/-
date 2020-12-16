import numpy as np
def solve1(file):
    with open(file, "r") as f:
        txt = f.read()
        print(txt.count(";"))
#solve1("txt1.txt")

def solve2(file):
    with open(file, "r") as f:
        txt = f.readlines()
        for index, t in enumerate(txt):
            if "main" in t:
                print(f"{index+1}: {t[:-1]}")
#solve2("txt2.txt")

def solve3(file):
    with open(file, "r") as f:
        tep = 0
        dup = False
        while 1:
            txt = f.readline()
            if txt == tep:
                dup = True
            else:
                if dup:
                    if tep[:-1]:
                        print(tep[:-1])
                    dup = False
            tep = txt
            if not txt:
                break
#solve3("txt3.txt")

def solve4(file):
    with open(file) as f:
        txt = f.readlines()
        dup = set()
        cnt = 0
        for i in range(len(txt)):
            if txt[i] in txt[i+1:] and txt[i] not in dup:
                if txt[i][:-1]:
                    cnt += 1
                    dup.add(txt[i])
                    print(txt[i][:-1])
        print(cnt)
#solve4("txt3.txt")

def solve5(file):
    with open(file) as f:
        text = f.readlines()
        txt = []
        max_len = 0
        for t in text:
            if t[-1] == "\n":
                txt.append(t[:-1])
                max_len = max(max_len, len(t[:-1]))
            else:
                txt.append(t)
                max_len = max(max_len, t)

        formatted_txt = np.array([[" " for _ in range(max_len)] for _ in range(len(txt))])
        for i, t in enumerate(txt):
            for j, ch in enumerate(t):
                formatted_txt[i][j] = ch
        ret = set()
        sames = 0
        for i in range(len(formatted_txt)-1):
            txt1 = formatted_txt[i]
            for j in range(i+1, len(formatted_txt)):
                txt2 = formatted_txt[j]
                bootleans = [txt1[i] == txt2[i] for i in range(max_len)]
                same_scores = sum(bootleans)
                if same_scores < max_len and (max_len-same_scores) < 5:
                    sames += 1
                    pair1 = "{0}, {1}".format("".join(txt1), "".join(txt2))
                    pair2 = "{0}, {1}".format("".join(txt2), "".join(txt1))
                    if pair1 not in ret and pair2 not in ret:
                        ret.add(pair1)
        
        for t in ret:
            print(t)
solve5("txt3.txt")