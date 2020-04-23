#Create lists in list to get a grid= 2D list
number_grid= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
#To access an element in 2D list, list[row][column]
#To get 1
print(number_grid[0][0])
#To get 8
print(number_grid[2][1])

#Nested for loops: for loops inside for loops
for row in number_grid:
    for column in row:
        print(column)
