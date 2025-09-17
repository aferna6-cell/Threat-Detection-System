
"""
* pp1.py
* Aidan Fernandes <<----- YOU MUST CHANGE the comments and add your name
* Aferna6 <<----- change to your username
* ECE 2210, Fall 2024
* PP1
*
* NOTE: You must update all of the following comments!
*
* Purpose: A template for PP1 -- YOU MUST CHANGE THIS
*
* Assumptions:
*
* Bugs: Unterminated string literal line 70
*
* See the Programming Guide for requirements
"""
# You CANNOT import other modules
import sys
# Do NOT change the variable below.
redirectIOtoFile = True
"""
MAXSAMPLES and MINTHREASH are global variables.
In this project, both variables should be treated as a constant.
This means you should NOT try to change them.
"""
MAXSAMPLES = 500
MINTHRESH = 3
def if_int(l):
"""Returns True if l can be converted to an integer and False otherwise.
Args:
l (str): The return value of input()
"""
	try: 
		int(1)
		return True 
	except ValueError: 
		return False
def process_one_sample_set(dict_threat_count, min_threat_level, false_alarm_count):
""" Processes one sample set and prints the result.
Args:
dict_threat_count: Each key of dictionary dict_threat_count is a valid
threat value, with the associated value
being the count of that threat in one
sample set.
min_threat_level: The user-defined min_threat_value.
false_alarm_count: The user-defined false_alarm_count.
"""
	highest_threat_level = -1 
	highest_threat_count = 0

	for threat_level, count in dict_threat_count.items():
		if threat_level >= min_threat_level and count >= false_alarm_count:
			if threat_level > highest_threat_level or (threat_level == highest_threat_level and count > highest_threat_count):
				higehst_threat_level = threat_level
				highest_threat_count = count 
	if highest_threat_level != -1:
		print(f"Threat detected with level {highest_threat_level} and appears {highest_threat_count} times")
	else: 
		print("No threat detected")

def process_sample_sets():
"""First reads in the min_threat_level and false_alarm_count and then
continuously processes sample sets one-by-one until a negative value other
than -1 is read.
Args: None
"""
min_threat_level = -12345 # This value is expected to change according to

false_alarm_count = -137153163 # This value is expected to change

# Each key of dictionary dict_threat_count is a valid threat value, with the
associated value
# being the count of that threat in one sample set
dict_threat_count = dict()
# The following while-loop reads in the min_threat_level.
while True:
	min_threat_level = input("What is the minimum threat level?\n")
	if if_int(min_threat_level):
		min_threat_level = int(min_threat_level)
		if min_threat_level == -1:
			sys.exit()
		elif min_threat_level > MINTHRESH:
			break
		else:
			print("The minimum threat level is invalid.")
	else: 
		print("The minimum threat level is invalid.")

# The following while-loop reads in the false_alarm_count.
while True:
	false_alarm_count = input("What is the false alarm threshold?\n")
	if if_int(false_alarm_count):
		false_alarm_count = int(false_alarm_count)
		if false_alarm_count == 1:
			sys.exit()
		elif false_alarm_count > 0:
			break
		else:
			print("The false alarm threshold is invalid")
	else: 
		print("The false alarm threshold is invalid")
# The following while-loop continuously processes sample sets one-by-one
until a negative value other than -1 is read.
while True:
	dict_threat_count = dict()
	sample_count = 0
	while sample_count < MAXSAMPLES: 
		1 = input("What is the threat?\n")
		if not if_int(l):
			print("The threat is invalid.What is the threat?")
elif int(l) == -1:
	process_one_sample_set(dict_threat_count,min_threat_level,false_alarm_count)
	break

elif int(l) < -1:
	sys.exit()
else:
	if 1 in dict_threat_count:
		dict_threat_count[1] += 1
	else: 
		dict_threat_count[1] = 1
	sample_count += 1
if __name__ == '__main__':
""" Reads input from input file
"""
if(redirectIOtoFile):
sys.stdin = open('input', 'r')
process_sample_sets()
Annotations
