interesting_numbers = []
for i in range(1, 100000):
    number = str(i) * 2
    interesting_numbers.append(number)

file_path = "input1.txt"
try:
    with open(file_path, 'r') as file:
        ans = 0
        for line in file:
            segments = line.split(",")
            for number in interesting_numbers:
                for segment in segments:
                    l, r = map(int, segment.split("-"))
                    if l <= int(number) <= r:
                        ans += int(number)

        print(ans)
except:
    pass
finally:
    pass