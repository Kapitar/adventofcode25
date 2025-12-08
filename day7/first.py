file_path = "input1.txt"

n = 0
m = 0
matrix = []

def dfs(i: int, j: int):
    global n, m, matrix

    if i + 1 >= n:
        return 0

    if matrix[i + 1][j] == "|":
        return 0

    if matrix[i + 1][j] == ".":
        matrix[i + 1][j] = "|"
        return dfs(i + 1, j)

    ans = 1
    if j - 1 >= 0:
        if matrix[i + 1][j - 1] != "|":
            matrix[i + 1][j - 1] = "|"
            ans += dfs(i + 1, j - 1)
    if j + 1 < m:
        if matrix[i + 1][j + 1] != "|":
            matrix[i + 1][j + 1] = "|"
            ans += dfs(i + 1, j + 1)

    return ans


with open(file_path, 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))

    n = len(matrix)
    m = len(matrix[0])

    # print(matrix)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'S':
                print(dfs(i, j))
                exit(0)
