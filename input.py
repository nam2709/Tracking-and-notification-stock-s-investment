import subprocess 
import time
from subprocess import call
# start = 1608525308
# end = 1642653368
print("mã:")
n = input()

print("1:")
a= input()
a = int(a)
b= 20000000000

print("2:")
c = input()
c = int(c)
d = c - a 
# d = 1608530242


file = open("am.txt", "w")

for sbd in range(a,b):
	z = sbd - a
	if (z%15 == 0):
		sbd = sbd
		time.sleep(15)
		command = 'curl https://iboard.ssi.com.vn/dchart/api/history?resolution=D&symbol='+ str(n) +'&from=' + str(sbd) + '&to=' + str(sbd+d)

		print(command)
		result = subprocess.check_output(command)
		file.write(str(result) + "\n")
		call(["python", "a.py"])