def main():
	#floating nums
	FloatNum1 = 2.4
	FloatNum2 = 3.4
	#integers
	Int1 = 4
	Int2 = 5

	#sum functionn
	sum_result = FloatNum1 + FloatNum2
	print_result('Sum:', sum_result)

	#diff function
	diff_result = Int1 - Int2
	print_result('Difference:', diff_result)

	#product function
	product_result = FloatNum1 * Int1
	print_result('Product:', product_result)

def print_result(operation, result):
	print(f'{operation}: {result}, Type: {type(result)}')

if __name__ == '__main__':
	main()
