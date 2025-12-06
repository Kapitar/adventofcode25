file_path = "input2.txt"

with open(file_path, 'r') as file:
    matrix = []
    for line in file:
        matrix.append(line.replace("\n", ""))

    ans = 0
    op = ""
    numbers = []
    for j in range(len(matrix[0])):
        flag = True
        number = ""
        for i in range(len(matrix)):
            if matrix[i][j] != " ":
                flag = False

            if matrix[i][j] == "*" or matrix[i][j] == "+":
                op = matrix[i][j]
            else:
                if matrix[i][j] != " ":
                    number += matrix[i][j]

        if flag:
            sum = 0
            mult = 1
            for number in numbers:
                sum += int(number)
                mult *= int(number)

            if op == "+":
                ans += sum
            else:
                ans += mult

            numbers = []
        else:
            numbers.append(number)

    sum = 0
    mult = 1
    for number in numbers:
        sum += int(number)
        mult *= int(number)

    if op == "+":
        ans += sum
    else:
        ans += mult

    print(ans)