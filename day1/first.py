file_path = "input1.txt"
try:
    with open(file_path, 'r') as file:
        cur = 50
        ans = 0
        for line in file:
            line = line.strip()
            pos, times = line[0], int(line[1:])
            if pos == "R":
                cur += times
            else:
                cur -= times

            cur %= 100
            if cur == 0:
                ans += 1

        print(ans)
except:
    pass
finally:
    pass