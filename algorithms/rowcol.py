rows = range(1,4)
cols = range(1,3)
for row in rows:
	for col in cols:
		print(row,col)
rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols] 
for cell in cells: 
	print( cell)
for row, col in cells:
	print(row,col)
