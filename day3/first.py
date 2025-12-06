file_path = "input1.txt"

try:
    with open(file_path, 'r') as file:
        ans = 0
        for line in file:
            # print(line)
            maxx = 0
            for i in range(0, len(line)):
                for j in range(i + 1, len(line)):
                    maxx = max(maxx, int(line[i] + line[j]))

            ans += maxx

        print(ans)
except:
    pass
finally:
    pass