import numpy as np
from tabulate import tabulate
from astropy.table import Table
def main():
	x = np.linspace(0,2*np.pi,1000)
	y = np.sin(x)

	table_data = [(a,b) for a, b in zip(x,y)]

	table_headers = ['x', 'sin(x)']
	print(tabulate(table_data, headers=table_headers, floatfmt='.3f'))

if __name__ == '__main__':
	main()