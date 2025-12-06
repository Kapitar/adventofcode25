file_path = "input1.txt"

with open(file_path, 'r') as file:
    matrix = []
    for line in file:
        if not line.strip()[0].isdigit():
            matrix.append(line.strip().split())
        else:
            line = list(map(int, line.strip().split()))
            matrix.append(line)

    # print(matrix)
    ans = 0

    for j in range(len(matrix[0])):
        mult = 1
        sum = 0
        for i in range(len(matrix) - 1):
            sum += matrix[i][j]
            mult *= matrix[i][j]

        if matrix[len(matrix) - 1][j] == "*":
            ans += mult
        else:
            ans += sum

    print(ans)