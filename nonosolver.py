def main():
	p = puzzle('sunset')
	rows = p['rows']
	cols = p['cols']
	n = Nonogram(rows, cols)
	print(n)


def puzzle(name):
	puzzle = {
		'giraffe': {
			'rows': [(1,1),(2,1,1,2),(7,),(1,3),(6,),(7,),(8,),(8,),(8,),(4,)],
			'cols': [(1,),(2,),(8,),(3,6),(8,),(10,),(7,),(2,5),(1,4),(3,)]
		},
		'sunset': {
			'rows': [(1,1,2,1,1),(1,1,2,1),(1,1,2,1),(4,1),(3,),(1,),(1,1),(1,),(1,),(10,)],
			'cols': [(1,1),(1,1),(1,1,1,1),(1,1,1),(1,2,1),(2,2,1),(9,),(1,1,1,1),(1,1,1),(1,1,1)],
			'grid': 
				[
					[1,0,1,0,1,1,0,1,0,1],
					[0,1,0,1,0,1,1,0,1,0],
					[0,0,1,0,1,0,1,1,0,1],
					[0,0,0,1,1,1,1,0,1,0],
					[0,0,0,0,0,1,1,1,0,0],
					[0,0,0,0,0,0,1,0,0,0],
					[0,0,1,0,0,0,1,0,0,0],
					[0,0,0,0,0,0,1,0,0,0],
					[0,0,0,0,0,0,1,0,0,0],
					[1,1,1,1,1,1,1,1,1,1],
				]
		},
		'soccer': {
			'rows': [(3,),(5,),(3,1),(2,1),(3,3,4),(2,2,7),(6,1,1),(4,2,2),(1,1),(3,1),(6,),(2,7),(6,3,1),(1,2,2,1,1),(4,1,1,3),(4,2,2),(3,3,1),(3,3),(3,),(2,1)],
			'cols': [(2,),(1,2),(2,3),(2,3),(3,1,1),(2,1,1),(1,1,1,2,2),(1,1,3,1,3),(2,6,4),(3,3,9,1),(5,3,2),(3,1,2,2),(2,1,7),(3,3,2),(2,4),(2,1,2),(2,2,1),(2,2),(1,),(1,)]
		}
	}
	return puzzle[name]


def solve(nng):
	# Mathematical Fill Rows/Cols
	nng.grid = fill(nng, isrow=True)
	nng.grid = fill(nng, isrow=False)

	# Boxes
	return

def fill_line(line, clue):
	pass

def fill(nng, isrow):
	grid = nng.grid
	size = nng.size
	
	for i in range(size):
		line = nng.rows[i] if isrow else nng.cols[i]
		total = sum(line)
		diff = size-total
		fill = [x-diff for x in line]
		
		pos = 0
		for j, v in enumerate(line):
			pos += v
			start = pos - fill[j]
			for k in range(start, pos):
				if isrow:
					grid[i][k] = 1
				else:
					grid[k][i] = 1
			pos += j
	return grid

def boxes(nng):
	pass

def spaces(nng):
	pass

def forcing(nng):
	pass

def glue(nng):
	pass

def joinsplit(nng):
	pass

def puntuate(nng):
	pass

def mercury(nng):
	pass

def contradict(nng):
	pass

def guess(nng):
	pass


def pretty_print(nng):
	BLOCK = u'\u2588\u2588' # ASCII char for cells that are filled
	BLANK = '  '            # ASCII char for cells that are empty
	NONE  = '__'            # ASCII char for cells that are undiscovered
	n = len(nng.grid)  # Size of grid

	# Row clues
	rsize = max([len(i) for i in nng.rows]) * 2
	row_clues = [' '.join(map(lambda x: str(x), i)).rjust(rsize, ' ') for i in nng.rows]

	# Column clues
	csize = max([len(i) for i in nng.cols])
	col_clues = [' '.rjust(rsize+1, ' ') for i in range(csize)]
	for j in nng.cols:
		for i in range(1, csize+1):
			col_clues[-i] += str(j[-i]).rjust(2, ' ') if len(j) >= i else '  '
			
	# Grid
	for i in col_clues:
		print(i)

	grid = ''
	for i in range(n):
		grid += row_clues[i] + ' '
		for j in range(n):
			if nng.grid[i][j] == 1:    grid += BLOCK
			if nng.grid[i][j] == 0:    grid += BLANK
			if nng.grid[i][j] == None: grid += NONE
		grid += '\n'
	return grid

class Nonogram():
	# rows - Clues for each row in the grid
	# cols - Clues for each column in the grid

	def __init__(self, rows, cols):
		assert len(rows) == len(cols)
		self.rows = rows
		self.cols = cols
		self.size = len(rows)
		self.grid = [[None for r in range(self.size)] for c in range(self.size)]
		self.solve()

	def __str__(self):
		return pretty_print(self)

	def solve(self):
		return solve(self)


if __name__ == '__main__':
	main()	
