import os 
import csv 
from datetime import datetime, timedelta
import string
import regex
import numpy as np
import matplotlib.pyplot as plt

# filter_by_archive_status will take a bool is_archived and will return an array of all archived
# logs if is_archive is true, and an array of all non-archived logs if is-archived is false
def filter_by_archive_status(log_lines, is_archived):
    pass

# filter_by_time will take a time (date-time object) and will return an array of all logs 
# that were created AFTER and including the specified time 
def filter_by_time(time):
    pass

def read_files(logs_file):
    # Read in the file with all bug logs transcripts and store in log_lines 
    with open(logs_file, 'r') as f:
        log_lines = f.readlines()
    f.close()

    # Limit the logs to only being archived

    # Limit the logs to only being within the past year 

def output_CSV(fieldNames, finalList, fileName):
    with open(fileName, 'w') as csvfile: 
        # Creating a CSV writer object 
        csvwriter = csv.writer(csvfile) 
        
        # Writing the fields 
        csvwriter.writerow(fieldNames) 
        
        # Writing the data rows 
        csvwriter.writerows(finalList)

# Local path to Trello board bug logs 
local_data_path = '../../web_dev_bugs/web_dev_bugs.csv'
read_files(local_data_path)