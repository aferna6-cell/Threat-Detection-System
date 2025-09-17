# Threat Detection System

Real-time threat monitoring system with configurable alert thresholds and statistical analysis. Implements data sampling, threat level classification, false alarm filtering, and continuous monitoring with user-defined security parameters.

## Overview

This Python program simulates a real-time threat detection and monitoring system. It processes streams of threat level data, applies user-defined filtering criteria, and identifies the most significant threats while minimizing false alarms through statistical analysis and threshold-based filtering.

## Features

### Real-Time Processing
- **Continuous monitoring**: Processes threat data in real-time streams
- **Sample set analysis**: Groups data into manageable sample sets (up to 500 samples)
- **Immediate alerts**: Provides instant threat detection notifications
- **Configurable thresholds**: User-defined minimum threat levels and alarm counts

### Statistical Analysis
- **Frequency counting**: Tracks occurrence of each threat level
- **Threshold filtering**: Eliminates low-significance threats
- **False alarm reduction**: Requires minimum occurrence counts
- **Highest threat prioritization**: Identifies most severe threats first

### System Configuration
- **Minimum threat level**: Configurable lower bound (must be > 3)
- **False alarm threshold**: Minimum occurrence count for valid threats
- **Sample limits**: Maximum 500 samples per analysis set
- **Input validation**: Comprehensive error checking and user feedback

## Technical Implementation

### Core Constants
```python
MAXSAMPLES = 500    # Maximum samples per set
MINTHRESH = 3       # Minimum allowable threat threshold
```

### Threat Detection Algorithm
```python
def process_one_sample_set(dict_threat_count, min_threat_level, false_alarm_count):
    1. Initialize highest threat tracking variables
    2. For each threat level in sample set:
       a. Check if meets minimum threat level
       b. Check if meets false alarm threshold
       c. Update highest threat if more severe
    3. Report highest valid threat or no threat detected
```

### Data Processing Flow
```python
def process_sample_sets():
    1. Read and validate minimum threat level
    2. Read and validate false alarm threshold  
    3. Continuously process sample sets:
       a. Initialize new sample set
       b. Read threat values until -1 or max samples
       c. Build frequency distribution
       d. Analyze and report results
    4. Exit on negative values < -1
```

## Input/Output Protocol

### Configuration Phase
```
What is the minimum threat level?
> 5
What is the false alarm threshold?
> 2
```

### Threat Data Processing
```
What is the threat?
> 7
What is the threat?
> 5
What is the threat?
> 7
What is the threat?
> -1
Threat detected with level 7 and appears 2 times
```

### Control Codes
- **-1**: End current sample set and process
- **< -1**: Exit program
- **Non-integers**: Invalid input, prompt for retry

## Usage

### Running the System
```bash
python3 pp1.py
```

### Input File Format
Create an 'input' file with configuration and threat data:
```
5
2
7
5
7
8
8
8
-1
-2
```

### Expected Output
```
What is the minimum threat level?
What is the false alarm threshold?
What is the threat?
What is the threat?
What is the threat?
What is the threat?
What is the threat?
What is the threat?
Threat detected with level 8 and appears 3 times
```

## Validation Rules

### Minimum Threat Level
- Must be an integer
- Must be greater than MINTHRESH (3)
- Input of -1 exits the program
- Invalid inputs prompt for retry

### False Alarm Threshold
- Must be a positive integer
- Must be greater than 0
- Input of -1 exits the program
- Invalid inputs prompt for retry

### Threat Values
- Must be integers
- Negative values < -1 exit program
- -1 triggers sample set processing
- Non-integers are rejected with error message

## Algorithm Analysis

### Time Complexity
- **Sample processing**: O(n) where n = number of samples
- **Threat analysis**: O(k) where k = unique threat levels
- **Overall complexity**: O(n + k) per sample set

### Space Complexity
- **Threat counting**: O(k) for unique threat levels
- **Input validation**: O(1) for temporary storage
- **Memory usage**: Linear with threat level diversity

### Performance Characteristics
- **Sample limit**: 500 samples maximum per set
- **Dictionary operations**: O(1) average for counting
- **Threshold filtering**: Constant time per threat level

## Security Applications

### Network Monitoring
- **Intrusion detection**: Monitor network traffic anomalies
- **DDoS protection**: Identify attack patterns
- **Traffic analysis**: Statistical threat assessment

### System Security
- **Log analysis**: Process security event logs
- **Anomaly detection**: Identify unusual system behavior
- **Risk assessment**: Quantify threat severity levels

### Real-Time Response
- **Alert generation**: Immediate threat notifications
- **Escalation procedures**: Priority-based response
- **Threshold tuning**: Adaptive sensitivity control

## Error Handling

### Input Validation
```python
def is_int(l):
    try: 
        int(l)
        return True 
    except ValueError: 
        return False
```

### User Feedback
- **Clear error messages**: Descriptive validation failures
- **Retry mechanisms**: Continuous input prompting
- **Graceful exits**: Clean program termination on control codes

## Fixed Issues from Original Code

The original code contained multiple critical errors:

1. **Function name**: `if_int` renamed to `is_int` (more conventional)
2. **Logic error**: `int(1)` changed to `int(l)` for actual parameter validation
3. **Variable typo**: `higehst_threat_level` corrected to `highest_threat_level`
4. **Syntax errors**: Fixed unterminated strings and indentation
5. **Variable naming**: Fixed `1` to `l` (variables can't start with numbers)
6. **Logic flow**: Corrected control flow and exit conditions
7. **Input handling**: Proper variable assignment and validation

## Educational Applications

### Computer Security
- **Threat modeling**: Understanding attack patterns
- **Risk assessment**: Quantitative security analysis
- **Monitoring systems**: Real-time security operations

### Data Processing
- **Stream processing**: Real-time data analysis
- **Statistical filtering**: Noise reduction techniques
- **Threshold-based decisions**: Automated classification systems

### Software Engineering
- **Input validation**: Robust error handling
- **State management**: Program flow control
- **Configuration systems**: User-defined parameters

## Author
Aidan Fernandes  
ECE 2210 - Fall 2024  
Clemson University

## Educational Context
This project demonstrates:
- Real-time data processing and analysis
- Statistical filtering and threshold-based decision making
- Input validation and error handling
- Dictionary-based frequency analysis
- Security monitoring system principles
