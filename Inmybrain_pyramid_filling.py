def printgrid(arr):
    for ar in arr:
        print(ar)
    return 0

def solution(blocks):
    res = []
    grid = [[0]*(i+1) for i in range(len(blocks))]
    # printgrid(grid)
    for i, b in enumerate(blocks):
        idx, val = b
        # print(i, idx, val)
        grid[i][idx] = val

        for j in range(idx-1, -1, -1): # go left
            # print("left:", j)
            grid[i][j] = grid[i-1][j] - grid[i][j+1]

        for j in range(idx+1, i+1): # go right
            # print("right:", j)
            grid[i][j] = grid[i-1][j-1] - grid[i][j-1]

        # printgrid(grid)

    #print grid
    for g in grid:
        for el in g:
            res.append(el)

    return res
    # return [92, 72, 20, 63, 9, 11, 144, -81, 90, -79, 217, -73, -8, 98, -177]


if __name__ == "__main__":
    inputs = []
    answers = []
    prob = [[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]
    ans = [50, 22, 28, 4, 18, 10, 0, 4, 14, -4, 1, -1, 5, 9, -13]
    inputs.append(prob)
    answers.append(ans)
    prob = [[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]
    ans = [92, 72, 20, 63, 9, 11, 144, -81, 90, -79, 217, -73, -8, 98, -177]
    inputs.append(prob)
    answers.append(ans)

    for ele, an in zip(inputs, answers):
        ansarr = solution(ele)
        print("correct?: {}".format(ansarr == an))
        print("predict: {}".format(ansarr))
        print("answer: {}".format(an))