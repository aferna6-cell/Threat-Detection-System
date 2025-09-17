"""
* pp1.py
* Aidan Fernandes
* Aferna6
* ECE 2210, Fall 2024
* PP1
*
* Purpose: Real-time threat monitoring system with configurable alert thresholds 
* and statistical analysis. Implements data sampling, threat level classification, 
* false alarm filtering, and continuous monitoring with user-defined security parameters.
*
* Assumptions:
* - Input file contains valid integer threat levels and control codes
* - User provides valid threshold and alarm count parameters
* - System processes up to MAXSAMPLES per sample set
*
* Bugs: None known (fixed from original)
*
* See the Programming Guide for requirements
"""

# You CANNOT import other modules
import sys

# Do NOT change the variable below.
redirectIOtoFile = True

"""
MAXSAMPLES and MINTHRESH are global variables.
In this project, both variables should be treated as a constant.
This means you should NOT try to change them.
"""
MAXSAMPLES = 500
MINTHRESH = 3

def is_int(l):
    """Returns True if l can be converted to an integer and False otherwise.
    Args:
        l (str): The return value of input()
    """
    try: 
        int(l)
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
                highest_threat_level = threat_level
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
    min_threat_level = -12345  # This value is expected to change according to user input
    false_alarm_count = -137153163  # This value is expected to change according to user input

    # Each key of dictionary dict_threat_count is a valid threat value, with the associated value
    # being the count of that threat in one sample set
    dict_threat_count = dict()
    
    # The following while-loop reads in the min_threat_level.
    while True:
        min_threat_level_input = input("What is the minimum threat level?\n")
        if is_int(min_threat_level_input):
            min_threat_level = int(min_threat_level_input)
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
        false_alarm_count_input = input("What is the false alarm threshold?\n")
        if is_int(false_alarm_count_input):
            false_alarm_count = int(false_alarm_count_input)
            if false_alarm_count == -1:
                sys.exit()
            elif false_alarm_count > 0:
                break
            else:
                print("The false alarm threshold is invalid.")
        else: 
            print("The false alarm threshold is invalid.")
            
    # The following while-loop continuously processes sample sets one-by-one
    # until a negative value other than -1 is read.
    while True:
        dict_threat_count = dict()
        sample_count = 0
        
        while sample_count < MAXSAMPLES: 
            l = input("What is the threat?\n")
            if not is_int(l):
                print("The threat is invalid.")
                continue
            
            threat_value = int(l)
            
            if threat_value == -1:
                process_one_sample_set(dict_threat_count, min_threat_level, false_alarm_count)
                break
            elif threat_value < -1:
                sys.exit()
            else:
                if threat_value in dict_threat_count:
                    dict_threat_count[threat_value] += 1
                else: 
                    dict_threat_count[threat_value] = 1
                sample_count += 1

if __name__ == '__main__':
    """ Reads input from input file """
    if(redirectIOtoFile):
        sys.stdin = open('input', 'r')
    process_sample_sets()
