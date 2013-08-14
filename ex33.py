def number_count(x, n):
	i = 0
	numbers = []
	
	while i < x:
		print "At the top i is %s" % i
		numbers.append(i)
		
		i = i + n
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
	print "The numbers: "

	for num in numbers:
		print num

number_count(14, 2)