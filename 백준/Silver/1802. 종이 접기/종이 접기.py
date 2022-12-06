def isAvailableStr(some_str: str):
    paper = list(some_str)

    while len(paper) >= 3:
        for i in range(2, len(paper), 2):
            if paper[i-2] == paper[i]:
                return False

        nextpaper = []
        for i in range(1, len(paper), 2):
            nextpaper.append(paper[i])

        paper = nextpaper

    return True


T = int(input())
for _ in range(T):
    paper_str = input()

    if isAvailableStr(paper_str):
        print("YES")
    else:
        print("NO")