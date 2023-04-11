def transfer(curr_x, curr_y, Prev_x, Prev_y, res, matrix, n):
    if curr_x < 0 or curr_y < 0 or curr_x > n-1 or curr_y > n-1:
        return False
    if matrix[curr_x][curr_y] == 0:
        return False
    if curr_x == Prev_x and curr_y == Prev_y:
        return False

    if curr_x == n-1 or curr_y == n-1:
        print(res)
        return True

    transfer(curr_x-1, curr_y, curr_x, curr_y, res+"L", matrix, n)
    transfer(curr_x+1, curr_y, curr_x, curr_y, res+"R", matrix, n)
    transfer(curr_x, curr_y-1, curr_x, curr_y, res+"D", matrix, n)
    transfer(curr_x, curr_y+1, curr_x, curr_y, res+"U", matrix, n)


matrix = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]

if not transfer(0, 0, -1, -1, "", matrix, 4):
    print("-1")
