file_path = "input2.txt"
try:
    with open(file_path, 'r') as file:
        cur = 50
        ans = 0
        for line in file:
            line = line.strip()
            pos, times = line[0], int(line[1:])

            if pos == "R":
                if cur == 0:
                    ans += times // 100
                elif cur + times >= 100:
                    ans += (times - (100 - cur)) // 100 + 1
                cur += times
            else:
                if cur == 0:
                    ans += times // 100
                elif cur - times <= 0:
                    ans += (times - cur) // 100 + (cur != 0)
                cur -= times

            cur %= 100

        print(ans)
except:
    pass
finally:
    pass