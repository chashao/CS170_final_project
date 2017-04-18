import math
import random
import string


with open('problem1.in', 'w+') as f1:

	P = random.randint(1, 2**8)
	M = random.randint(1, 2**8)
	R = random.randint(1, 2**8)

	f1.write(str(P) + '\n')
	f1.write(str(M) + '\n')
	
	C = random.randint(1, 1000)
	N = random.randint(1, 1000)
	f1.write(str(N) + '\n')
	f1.write(str(C) + '\n')

	i = 0
	while i < N:
		f1.write(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)) + '; ' + str(random.randint(0, N - 1)) 
			+ '; '+ str(random.randint(0, P - 1)) + '; '+ str(random.randint(0, M - 1)) + '; ' + str(random.randint(0, R - 1)) + '\n')
		i += 1
	j = 0
	while j < C:
		f1.write(str(random.sample(range(N), random.randint(2, N)))[1: -1] + '\n')
		j += 11

with open('problem2.in', 'w+') as f2:

	P = random.randint(1, 2**8)
	M = random.randint(1, 2**8)
	R = random.randint(1, 2**8)

	f2.write(str(P) + '\n')
	f2.write(str(M) + '\n')

	C = random.randint(1, 1000)
	N = random.randint(1, 1000)

	f2.write(str(N) + '\n')
	f2.write(str(C) + '\n')

	i = 0
	while i < N:
		f2.write(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9)) + '; ' + str(random.randint(0, N - 1)) 
			+ '; '+ str(random.randint(0, P - 1)) + '; '+ str(random.randint(0, M - 1)) + '; ' + str(random.randint(0, R - 1)) + '\n')
		i += 1
	j = 0
	while j < C:
		f2.write(str(random.sample(range(N), random.randint(2, N)))[1: -1] + '\n')
		j += 1




with open('problem3.in', 'w+') as f3:

	P = random.randint(1, 2**8)
	M = random.randint(1, 2**8)
	R = random.randint(1, 2**8)

	f3.write(str(P) + '\n')
	f3.write(str(M) + '\n')

	C = random.randint(1, 1000)
	N = random.randint(1, 1000)

	f3.write(str(N) + '\n')
	f3.write(str(C) + '\n')

	i = 0
	while i < N:
		f3.write(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9)) + '; ' + str(random.randint(0, N - 1)) 
			+ '; '+ str(random.randint(0, P - 1)) + '; '+ str(random.randint(0, M - 1)) + '; ' + str(random.randint(0, R - 1)) + '\n')
		i += 1
	j = 0
	while j < C:
		f3.write(str(random.sample(range(N), random.randint(2, N)))[1: -1] + '\n')
		j += 1