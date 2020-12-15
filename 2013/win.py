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

#print1(solve1("txt1.txt"))

def solve2(file):
    txts = solve1(file)
    all = set()
    groups = []
    for txt in txts:
        als = txt.split("&")
        group = []
        for al in als:
            group.append(al)
            all.add(al)
        group.sort()
        groups.append(group)

    all2 = sorted(list(all))
    answer = set()
    for group in groups:
        ans = [""]
        for al in all2:
            if al in group:
                for i in range(len(ans)):
                    ans[i] += "{0}=true ".format(al)
            else:
                tmp = len(ans)
                ans = ans*2
                for i in range(tmp):
                    ans[i] += "{0}=true ".format(al)
                    ans[i+tmp] += "{0}=true ".format(al)
        for txt in ans:
            answer.add(txt)
    if len(answer) > 0:
        for a in answer:
            print(a)
    else:
        print("none")
    print(all, all2, groups)

solve2("txt1.txt")