def compute_d(phi_n,e):
	for i in range(1,1000):
		x = ((i*phi_n) + 1) / e
		y = (e*x) % phi_n
		if (y == 1) & (int(x)==x):
			print(x)
			break
compute_d(160,7)