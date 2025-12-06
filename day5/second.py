file_path = "input2.txt"

with open(file_path, 'r') as file:
    events = []
    for line in file:
        line = line.strip()
        l, r = map(int, line.split("-"))
        events.append((l, -1))
        events.append((r, 1))

    events.sort()

    cur = 0
    start = 0
    ans = 0
    for (x, type) in events:
        if type == -1 and cur == 0:
            start = x
        if type == -1:
            cur += 1
        else:
            cur -= 1
            if cur == 0:
                ans += x - start + 1

    print(ans)
