from random import shuffle
height = input("Enter the height of the rectangle:")
height = int(height)
width = input("Enter the width of the rectangle:")
width = int(width)

list1 = []

x = width/2
pl = int(x)
rest = width-pl
count = 0

for v in range(100):
    for j in range(height):
        examplelist = []
        examplelist = ["O"] * rest + ["S"] * pl
        shuffle(examplelist)
        list1.append(examplelist)

    for i in range(height):

        for j in range(width):

            if j <= width-3:

                if list1[i][j]=="S" and list1[i][j+1]=="O" and list1[i][j+2]=="S":

                    count = count + 1

            if i <= height-3:

                if list1[i][j]=="S" and list1[i+1][j]=="O" and list1[i+2][j]=="S":

                    count = count + 1

            if i <= height-3 and j <= width-3:
                if list1[i][j] == "S" and list1[i+1][j+1] == "O" and list1[i+2][j+2] == "S":
                    count = count + 1
            if i <= height-3 and j >= width-3:
                if list1[i][j] == "S" and list1[i+1][j-1] == "O" and list1[i+2][j-2] == "S":
                    count = count + 1

print ("the average number of groups is:")
print(count/100)
