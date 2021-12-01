num_of_station = int(input('Nhap so tram: '))

lst = []
for i in range(num_of_station):
	lst.append([0]*num_of_station)

for i in range(len(lst)):
	for c in range(len(lst[i])): 
		if i == c: 
			continue 
		else: 
			print('Nhap', chr(c+65), '-', chr(i+65), end=': ')
			lst[i][c] = int(input()) 

for i in range(num_of_station):
	print(lst[i])