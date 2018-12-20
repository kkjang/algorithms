def build_lookup_table():
	table = dict()
	table[0] = 0
	for i in range(256):
		table[i] = table[int(i/2)] + (i & 1)
	return table

TABLE = build_lookup_table()

def count_bits_set(n):
	return TABLE[n & 255] +TABLE[(n >> 8) & 255] + TABLE[(n >> 16) & 255] + TABLE[(n >> 24) & 255]

print(count_bits_set(124123))
