import csv
import os
import re

inputfile=open("C:/Users/reese/Documents/personal_projects/option_calculator/input.csv")
callfilepath="C:/Users/reese/Documents/personal_projects/option_calculator/formatted_data/calls"
putfilepath="C:/Users/reese/Documents/personal_projects/option_calculator/formatted_data/puts"

inputreader = csv.DictReader(inputfile)
i = 1
options = {}
# for row in inputreader:
# 	options.update({i : {'ticker' : row['ticker'], 'otype' : row['otype'], 'action' : row['action'], 'strike' : row['strike'], 'expiration' : row['expiration'], 'hold' : row['hold'], 'history' : row['history']}})
# 	i+=1
#print(options)

def dictget(dct, *keys):
	for key in keys:
		try:
			dct = dct[key]
		except KeyError:
			return None
	return dct


def natural_sort(l):
	convert = lambda text: int(text) if text.isdigit() else text
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
	l.sort( key=alphanum_key )


def binary_search(arr, x): 
	low = 0
	high = len(arr) - 1
	mid = 0
	while low <= high: 
		mid = (high + low) // 2
		# Check if x is present at mid 
		if arr[mid] < x: 
			low = mid + 1
		# If x is greater, ignore left half 
		elif arr[mid] > x: 
			high = mid - 1
		# If x is smaller, ignore right half 
		else: 
			return mid 
	# If we reach here, then the element was not present 
	return -1

def findnextdate(startdate, days):
	startday = int(startdate[8:10])
	#print("startdays is: " + str(startday))
	startmonth = int(startdate[5:7])
	startyear = int(startdate[0:4])
	monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	enddays = startday + days
	enddate = "date not found"
	#print("enddays is: " + str(enddays))
	if (enddays <= monthdays[startmonth - 1]):
		if(enddays < 10):
			strenddays = "0" + str(enddays)
		else: 
			strenddays = str(enddays)
		enddate = str(startyear) + "-" + str(startmonth) + "-" + strenddays
	elif(startmonth + 1 <= 12):
		enddays -= monthdays[startmonth-1]
		#print("enddays is: " + str(enddays))
		startmonth += 1
		if(enddays < 10):
			strenddays = "0" + str(enddays)
		else: 
			strenddays = str(enddays)
		enddate = str(startyear) + "-" + str(startmonth) + "-" + strenddays
	else:
		enddays -= monthdays[0]
		startyear += 1
		startmonth = 1
	#print(enddate)
	return(enddate)

def findprevdate(startdate, days):
	startday = int(startdate[8:10])
	#print("startdays is: " + str(startday))
	startmonth = int(startdate[5:7])
	startyear = int(startdate[0:4])
	monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	enddays = startday - days
	enddate = "date not found"
	#print("enddays is: " + str(enddays))
	while(True):
		if(enddays >= 365):
			startyear -= 1
			enddays -= 365
			continue
		print("enddays is: " + str(enddays))
		if(enddays >= monthdays[startmonth-1]): #add else statement to this
			if(startmonth - 1 > 0):
				enddays -= monthdays[startmonth-1]
				print("enddays is: " + str(enddays))
				startmonth -= 1
				if(enddays <= monthdays[startmonth-1]): 
					print("FINAL enddays is: " + str(enddays))
					if(enddays < 10):
						strenddays = "0" + str(enddays)
					else:
						strenddays = str(enddays)
						enddate = str(startyear) + "-" + str(startmonth) + "-" + strenddays
					break
			else: #finish this else statement
				if(enddays <= monthdays[startmonth-1]): 
					print("FINAL enddays is: " + str(enddays))
					if(enddays < 10):
						strenddays = "0" + str(enddays)
					else:
						strenddays = str(enddays)
						enddate = str(startyear) + "-" + str(startmonth) + "-" + strenddays
					break
				startyear -= 1
				enddays -= 31
		
	return(enddate)
print(findprevdate("2020-11-27", 20))
# #takes in a sorted filelist, a starting filename, and the number of days to expiration and returns the filename of closest day to expiration
# def findexpdata(filelist, startfile, expdays): #needs work, going to implement findnextdate to make it more efficient and compact
# 	#print(filelist)
# 	startday = int(startfile[-6:-4])
# 	#print("startdays is: " + str(startday))
# 	startmonth = int(startfile[-9:-7])
# 	startyear = int(startfile[-14:-10])
# 	starttype = startfile[0:4]
# 	monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 	enddays = startday + expdays
# 	#print("enddays is: " + str(enddays))
# 	if (enddays <= monthdays[startmonth - 1]):
# 		if(enddays < 10):
# 			strenddays = "0" + str(enddays)
# 		else: 
# 			strenddays = str(enddays)
# 		endfile = str(starttype) + "-" + str(startyear) + "-" + str(startmonth) + "-" + strenddays + ".csv"
# 	elif(startmonth + 1 <= 12):
# 		enddays -= monthdays[startmonth-1]
# 		startmonth += 1
# 		if(enddays < 10):
# 			strenddays = "0" + str(enddays)
# 		else: 
# 			strenddays = str(enddays)
# 		endfile = str(starttype) + "-" + str(startyear) + "-" + str(startmonth) + "-" + strenddays + ".csv"
# 		#print(endfile)
# 	else:
# 		enddays -= monthdays[0]
# 		startyear += 1
# 		startmonth = 1
# 	if(binary_search(filelist, endfile) >= 0):
# 		return(filelist[binary_search(filelist, endfile)])
# 	else:
# 		return("nofile")

# #need to give this parameters and make the main filename loop into a recursive call, also need to call the function afterwards in order for it to actually be run 
# def getprofit(options):
# 	inoptcount = 0
# 	outoptcount = 0
# 	initcost = 0
# 	exitcost = 0
# 	profit = 0
# 	targetstrike = 0
# 	opttype = 0 #0 is invalid, 1 is call, 2 is put
# 	stratprofits = {}
# 	for key in options:
# 		print("option key: " + str(key))
# 		if(dictget(options, key, 'otype') == 'C'):
# 			os.chdir(callfilepath)
# 			opttype = 1
# 			filelist = os.listdir()
# 			natural_sort(filelist)
# 		elif(dictget(options, key, 'otype') == 'P'):
# 			os.chdir(putfilepath)
# 			opttype = 2
# 			filelist = os.listdir()
# 			natural_sort(filelist)
# 		else:
# 			print("Wrong option type, try again")
# 		if(opttype > 0):
# 			for filename in filelist[::int(dictget(options, key, 'hold'))]:
# 				with open(filename, 'r') as incsvfile:
# 					expfilename = findexpdata(filelist, filename, int(dictget(options, key, 'hold')))
# 					if(expfilename != 'nofile'):
# 						initreader = csv.DictReader(incsvfile)
# 						row = next(initreader)
# 						targetexpiration = findnextdate(filename[5:15], int(options[key]['expiration']))
# 						#print("target expiration: " + str(targetexpiration))
# 						#print("infile: " + filename)
# 						#print("outfile: " + expfilename)
# 						for row in initreader:
# 							tprice = int(row['ticker_price'])
# 							expiration = row['expiration']
# 							optstrike = row['strike']
# 							optionprice = float(row['15:45_price'])
# 							targetstrike = int(tprice) + round(float(options[key]['strike'])/100 * tprice) #need to debug this and make sure its giving the correct values, also need to move it out of the loop so it doesnt recalculate for every line of the data
# 							#print("targetstrike: " + str(targetstrike))
# 							if(int(targetstrike) == int(optstrike)):	
# 								if(expiration == targetexpiration):
# 									inoptcount += 1
# 									initcost += optionprice
# 									break
# 						outcsvfile = open(expfilename, 'r')
# 						exitreader = csv.DictReader(outcsvfile)
# 						for row in exitreader:
# 							tprice = row['ticker_price']
# 							expiration = row['expiration']
# 							optstrike = row['strike']
# 							optionprice = float(row['15:45_price'])
# 							#print("optstrike: " + str(optstrike))
# 							if(int(targetstrike) == int(optstrike)):	
# 								if(expiration == targetexpiration):
# 									outoptcount += 1
# 									exitcost += optionprice
# 									break
# 			if(inoptcount == outoptcount):
# 				if(opttype == 1):
# 					print("exitcost = " + str(exitcost))
# 					print("initcost = " + str(initcost))
# 					profit = (exitcost - initcost)/inoptcount
# 				else:
# 					profit = (initcost - exitcost)/inoptcount
# 			print(profit)
# getprofit(options)
