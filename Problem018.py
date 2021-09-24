# This solution also works for #67
f = open("p067_triangle.txt", "r")
triangle = []
for line in f:
    line = line.split()
    row = []
    for item in line:
        row.append(int(item))
    triangle.append(row)
row_index = 0
answer = 0
for row in triangle:
    if row_index > 0:
        item_index = 0
        for item in row:
            #print("Row: {}\tItem: {}".format(row_index, item_index))
            if item_index == 0:
                triangle[row_index][0] = triangle[row_index - 1][0] + item
            elif item_index == len(row)-1:
                triangle[row_index][len(row)-1] = triangle[row_index - 1][len(triangle[row_index -
                1])-1] + item
            else:
                triangle[row_index][item_index] = max(triangle[row_index - 1][item_index-1],triangle[row_index - 1][item_index]) + item
            item_index += 1
    row_index += 1
    answer = max(row)
print(answer)
