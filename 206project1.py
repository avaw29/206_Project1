import os
import filecmp
import datetime

#Ava Weiner
#Worked with: Ben Crabtree, Rachel Brandes, we wrote the code alone and then went over our errors together.

def getData(fileName):
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

	#Your code here:
	f = open(fileName, "r")
	keys = f.readline().strip().split(",")
	lst = []
	for line in f.readlines():
		info = line.strip().split(",")
		datadict = {}
		my_index = 0
		for x in keys:
			datadict[x] = info[my_index]
			my_index += 1
		lst.append(datadict)
	return lst

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	srtd = sorted(data, key = lambda k: k[col])
	return srtd[0]["First"] + " " + srtd[0]["Last"]

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	counts = {'Senior': 0, 'Junior': 0, 'Sophomore': 0, 'Freshman': 0}

	for item in data:
		if item['Class'] == "Senior":
			counts['Senior'] += 1
		if item['Class'] == "Junior":
			counts['Junior'] += 1
		if item['Class'] == "Sophomore":
			counts['Sophomore'] += 1
		if item['Class'] == "Freshman":
			counts['Freshman'] += 1
	lst = []
	for key in counts.keys():
		lst.append((key, counts[key]))
	return sorted(lst, reverse = True, key = lambda k: k[1])


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	day_count = {}
	for item in a:
		day = item['DOB'].split('/')[1]
		if day not in day_count:
			day_count[day] = 0
		day_count[day] += 1
	lst = []
	for key in day_count.keys():
		tup = (key, day_count[key])
		lst.append(tup)
	srtd = sorted(lst, reverse = True, key = lambda k: k[1])
	return int(srtd[0][0])

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB to find their current age.

	#Your code here:
	today_month = datetime.date.today().month
	today_day = datetime.date.today().day
	today_year = datetime.date.today().year

	ages = []
	for person in a:
		dob = person["DOB"]
		month = dob.split("/")[0]
		day = dob.split("/")[1]
		year = dob.split("/")[2]
		if (int(month) < int(today_month)) and (int(day) < int(today_day)):
			age = (int(today_year) - int(year))
		else:
			age = int(today_year) - int(year) + 1
		ages.append(age)
	average = (sum(ages))/(len(ages))
	return int(average)

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	csv = open(fileName, "w")
	srtd = sorted(a, key = lambda k: k[col])
	for element in srtd:
		lst = []
		for item in element.values():
			lst.append(item)
		line = ",".join(lst[:3])
		csv.write(line + "\n")

	csv.close()
	return None

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
