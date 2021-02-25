from random import shuffle
measurement = input("Enter the size of the square:")
measurement = int(measurement)

list1 = []

x = measurement/2
pl = int(x)
rest = measurement-pl
count=0

for v in range(100):
	for j in range(measurement):
		examplelist = []
		examplelist = [0] * rest + [1] * pl
		shuffle(examplelist)
		list1.append(examplelist)

	for i in range(measurement):

		for j in range(measurement):

			if j <= measurement-4:

				if list1[i][j]==1 and list1[i][j+1]==1 and list1[i][j+2]==1 and list1[i][j+3]==1:

					count = count + 1

			if i <= measurement-4:

				if list1[i][j]==1 and list1[i+1][j]==1 and list1[i+2][j]==1 and list1[i+3][j]==1:

					count = count + 1

			if i <= measurement-4 and j <= measurement-4:
				if list1[i][j] == 1 and list1[i+1][j+1] == 1 and list1[i+2][j+2] == 1 and list1[i+3][j+3] == 1:
					count = count + 1
			if i <= measurement-4 and j >= measurement-4:
				if list1[i][j] == 1 and list1[i+1][j-1] == 1 and list1[i+2][j-2] == 1 and list1[i+3][j-3] == 1:
					count = count + 1

print ("the average number of groups is:")
print (count/100)
