def add(x, y):
	x + y

def subtract(x, y):
	return x-y

def divide(x, y):
	if y == 0:
		raise ValueError("Can not divide by zero")
	return x/y

def multiply(x, y):
	return x * y

def floor(x, y):
	if y == 0:
		raise ValueError("Can not divide by zero.")
	x // y
