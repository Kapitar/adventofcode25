file_path = "input1.txt"

with open(file_path, 'r') as file:
    segs = []
    reqs = []
    for line in file:
        line = line.strip()
        if line.find("-") != -1:
            l, r = map(int, line.split("-"))
            segs.append((l, r))
        else:
            x = int(line)
            reqs.append(x)

    ans = 0
    for req in reqs:
        for (l, r) in segs:
            if l <= req <= r:
                ans += 1
                break

    print(ans)