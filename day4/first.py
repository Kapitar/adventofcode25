file_path = "input1.txt"

with open(file_path, 'r') as file:
    matrix = []
    for line in file:
        matrix.append(line.strip())

    ans = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != "@":
                continue

            cnt = -1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    new_x = i + dx
                    new_y = j + dy

                    if new_x >= 0 and new_y >= 0 and new_x < len(matrix) and new_y < len(matrix[0]):
                        cnt += matrix[new_x][new_y] == "@"
            ans += (cnt < 4)

    print(ans)