import subprocess 
import csv
from subprocess import call
import time

file = open("am.txt", "r")

datas = file.read().split("\n")

for data in datas:

	data = data.replace("[","")
	data = data.replace("]","")
	data = data.replace("}","")
	data = data.replace("{","")
	data = data.replace('"' , '')
	data = data.replace(':' , ',')
	data = data.replace(",","\r")

	data = data.split()

	for i in range(len(data)):
		if data[i] == "o":
			begin = i
		if data[i] == "v":
			end = i
			cl = data[begin:end]

			for j in range(len(cl)):
					if cl[j] == "h":
						b= j
						nlt = cl[:b]

			for h in range(len(cl)):
					if cl[h] == "c":
						e = h
						nlg = cl[e:]

	with open("cr9.csv", "a", encoding='utf-8', newline='') as file_csv:
		
			writer = csv.writer(file_csv)
			writer.writerow(nlt)
			writer.writerow(nlg) 

	e0= float(nlt[-1])
	e1= float(nlt[-2])
	e6= float(nlt[-6])
	e2= float(nlt[-12])
	e3= float(nlt[-24])
	e4= float(nlt[-48])
	e5= float(nlt[-72])
	e8 = float(nlt[-154])

	d0= float(nlg[-1])
	d1= float(nlg[-2])
	d6= float(nlg[-6])
	d2= float(nlg[-12])
	d3= float(nlg[-24])
	d4= float(nlg[-48])
	d5= float(nlg[-72])
	d8= float(nlg[-154])


	a1 = (d0-e0)/e0 * 100
	a1 = round(a1,3)

	# if a1 >= 0:
	# 	call(["python", "em.py"])

	a2 = (e0 - e1)/e1 * 100
	a3 = (e0 - e6)/e6 * 100
	a4 = (e0 - e2)/e2 * 100
	a5 = (e0 - e3)/e3 * 100
	a6 = (e0 - e4)/e4 * 100
	a7 = (e0 - e5)/e5 * 100
	a8 = (e0 - e6)/e6 * 100

	a2 = round(a2,3)
	a3 = round(a3,3)
	a4 = round(a4,3)
	a5 = round(a5,3)
	a6 = round(a6,3)
	a7 = round(a7,3)
	a8 = round(a8,3)

	file1 = open("cr9.csv", "r", encoding='utf-8')
	file1 = open("cr9.csv", "a", encoding='utf-8')



	file1.write("\n"+"In day" + "," + str(a1) + "\n" + "Open compare to yesterday" + "," + str(a2) + "\n" + "Open compare to last week" + "," + str(a3) + "\n" + "Open compare to 2 weeks ago" + "," + str(a4) + "\n" + "Open compare to 1 month" + "," + str(a5) + "\n"  + "Open compare to 2 months ago" + "," + str(a6) + "\n" + "Open compare to 3 months ago" + "," + str(a7) + "\n" + "Open compare to 6 months ago" + "," + str(a8) + "\n"+"\n"+"\n"+ "NEWNEWNEWNEWNEWNEW" + "\n")


	print(a1)

