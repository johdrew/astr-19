def f(x):
	return x**3 + 8
	
def main():
	print('f(x) = x**3 + 8')
	result = f(9)
	print('Result: f(9) = ', result)

	if result > 27: 
		print('YAY!')

if __name__ == '__main__':
	main()