interesting_numbers = []
for i in range(1, 50000):
    for j in range(2, 20):
        number = str(i) * j
        interesting_numbers.append(number)

file_path = "input2.txt"
try:
    with open(file_path, 'r') as file:
        ans = 0
        found = []
        for line in file:
            segments = line.split(",")
            for number in interesting_numbers:
                for segment in segments:
                    l, r = map(int, segment.split("-"))
                    if l <= int(number) <= r and int(number) not in found:
                        found.append(int(number))
                        ans += int(number)

        print(ans)
except:
    pass
finally:
    pass