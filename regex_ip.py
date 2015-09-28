import re
# with open('ipconfig.txt', 'r') as f:
# 	ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', f.read() )
# 	print ip

with open('ipconfig.txt', 'r') as f:
	ip = []
	for line in f:
		print line
		ip.append(re.findall( r'[0-9]+(?:\.[0-9]+){3}', line))
	print [x for x in ip if x]