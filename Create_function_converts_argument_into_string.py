def func(**args):
	for a in args:
		print(a, args[a])


func(a=2, b=3)

''' I want the following work like above code'''
s = 'a=2, b=3'
func(s)