from bs4 import BeautifulSoup

import scipy.interpolate
import urllib2


import requests

def chomp(x):
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n"): return x[:-1]
    return x

def scrape(name):

	firstpart = "http://webbook.nist.gov/cgi/cbook.cgi?Name="
	secondpart = "&Units=SI&cTG=on&cTC=on&cTP=on&cTR=on&cSO=on"
	url = firstpart+str(name)+secondpart
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)
	print name

	STRUCTFILE = 'NA'
	MF = 'NA'
	MW = 'NA'


	#Molecular Weight
	try:
		main = soup.find('main',{'id' : 'main'})
		uls = main.findAll('ul')
		lis = uls[0].findAll('li')
		lis[1].strong.extract()
		lis[0].strong.extract()
		a_s = lis[7].findAll('a')
		a = a_s[2]

		try:
			STRUCTFILE = urllib2.urlopen('http://webbook.nist.gov'+a['href']).read()
		except: 
			STRUCTFILE = 'NA'

		try:
			MW = lis[1].text.strip()
		except:
			MW = 'NA'

		try:
			MF = lis[0].text.strip()
		except:
			MF = 'NA'

	except:
		pass

	#Heat cap of gas
	try:
		table = soup.find('table', {'aria-label' : 'Constant pressure heat capacity of gas'})

		x = []
		y = []

		for row in table.find_all('tr', {'class':'cal'}):
			t = row.find_all('td')
			y.append(float(t[0].text))
			x.append(float(t[1].text.strip().rstrip('.')))

		y_interp = scipy.interpolate.interp1d(x, y)
		CPV = y_interp(298)
	except:
		CPV = "NA"

	#Heat cap of liquid
	try:
		table = soup.find('table', {'aria-label' : 'Constant pressure heat capacity of liquid'})

		x = []
		y = []

		for row in table.find_all('tr', {'class':'exp'}):
			t = row.find_all('td',{'class':'right-nowrap'})
			y.append(float(t[0].text))
			x.append(float(t[1].text))

		y_interp = scipy.interpolate.interp1d(x, y)
		CPL = y_interp(298)
	except:
		CPL = "NA"

	#Heat cap of liquid
	try:
		table = soup.find('table', {'aria-label' : 'One dimensional data'})

		rows = table.find_all('tr', {'class':'exp'})
		t = rows[0].find('td',{'class':'right-nowrap'})
		FHG = float(t.text.split()[0])

	except:
		FHG = "NA"

	table = soup.find_all('table', {'aria-label' : 'One dimensional data'})
	#Heat cap of liquid
	try:

		rows = table[0].find_all('tr', {'class':'exp'})
		t = rows[0].find('td',{'class':'right-nowrap'})
		FHG = float(t.text.split()[0])

	except:
		FHG = "NA"

	#Heat cap of liquid
	try:
		rows = table[1].find_all('tr', {'class':'exp'})
		t = rows[0].find('td',{'class':'right-nowrap'})
		FHL = float(t.text.split()[0])

	except:
		FHL = "NA"

	#Heat cap of liquid
	try:
		rows = table[2].find_all('tr', {'class':'cal'})
		TB = float(rows[0].find('td',{'class':'right-nowrap'}).text.split()[0])
	except:
		TB = "NA"
	try:
		TF = float(rows[1].find('td',{'class':'right-nowrap'}).text.split()[0])
	except:
		TF = "NA"
	try:
		TT = float(rows[2].find('td',{'class':'right-nowrap'}).text.split()[0])
	except:
		TT = "NA"
	try:
		TC = float(rows[3].find('td',{'class':'right-nowrap'}).text.split()[0])
	except:
		TC = "NA"
	try:
		PC = float(rows[4].find('td',{'class':'right-nowrap'}).text.split()[0])
	except:
		PC = "NA"
	try:
		VC = float(rows[5].find('td',{'class':'right-nowrap'}).text.split()[0])
	except:
		VC = "NA"
	try:
		RHOC = float(rows[6].find('td',{'class':'right-nowrap'}).text.split()[0])
	except:
		RHOC = "NA"
	try:
		HVAP = float(rows[7].find('td',{'class':'right-nowrap'}).text.split()[0])
	except:
		HVAP = "NA"
	try:
		rows = table[2].find_all('tr', {'class':'exp'})
		HSUB = float(rows[0].find('td',{'class':'right-nowrap'}).text.split()[0])
	except:
		HSUB = "NA"



	try:
		table = soup.find('table', {'aria-label' : 'Enthalpy of fusion'})

		x = []
		y = []

		for row in table.find_all('tr', {'class':'exp'}):
			t = row.find_all('td',{'class':'right-nowrap'})
			y.append(float(t[0].text))
			x.append(float(t[1].text))

		y_interp = scipy.interpolate.interp1d(x, y)
		HFUS = y_interp(TF)
	except:
		HFUS = "NA"

	try:
		table = soup.find('table', {'aria-label' : 'Entropy of fusion'})

		x = []
		y = []

		for row in table.find_all('tr', {'class':'exp'}):
			t = row.find_all('td',{'class':'right-nowrap'})
			y.append(float(t[0].text))
			x.append(float(t[1].text))

		y_interp = scipy.interpolate.interp1d(x, y)
		SFUS = y_interp(TF)
	except:
		SFUS = "NA"

	try:
		table = soup.find('table', {'aria-label' : 'Antoine Equation Parameters'})

		x = []
		y1 = []
		y2 = []
		y3 = []

		for row in table.find_all('tr', {'class':'exp'}):
			t = row.find_all('td',{'class':'right-nowrap'})
			x.append(float(t[0].text.split()[0]))
			y1.append(float(t[1].text))
			y2.append(float(t[2].text))
			y3.append(float(t[3].text))


		y_interp1 = scipy.interpolate.interp1d(x, y1)
		A = y_interp1(298)
		y_interp2 = scipy.interpolate.interp1d(x, y2)
		B = y_interp2(298)
		y_interp3 = scipy.interpolate.interp1d(x, y3)
		C = y_interp3(298)
	except:
		A = "NA"
		B = "NA"
		C = "NA"


	return [name, MF, MW, CPV, CPL, FHG, FHL, TB, TF, TT, TC, PC, VC, RHOC, HVAP, HSUB , HFUS, SFUS, A, B, C, STRUCTFILE]


f = open('compounds.txt', 'r')


import csv
writer = csv.writer(open('dataset.csv', 'w'))
writer.writerow(['NAME', 'MF', 'MW', 'CPV', 'CPL', 'FHG', 'FHL', 'TB', 'TF', 'TT', 'TC', 'PC', 'VC', 'RHOC', 'HVAP', 'HSUB' , 'HFUS', 'SFUS', 'A' ,'B', 'C', 'STRUCTFILE'])
for name in f:
	row = scrape(chomp(name))
	writer.writerow(row)
