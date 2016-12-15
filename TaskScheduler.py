# Next step is to enter in some validation to restrict waht fields can contain,
# and to be unable to produce invalid batch files.

## Version 2.0
## Addition of data validation checks and error handling. 

from subprocess import Popen
import time
import os
import re
import sys


folder = os.getcwd()

# Check that time entry is in 24 hour clock.

time_re = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
def is_time_format(s):
    return bool(time_re.match(s))


# Check that the batch file is in the user defined folder.

def file_exists(file):
    folder, file = file.rsplit('/', 1)
    chk_folder = os.listdir(folder)
    if file in chk_folder:
        return True
    else:
        print (FileNotFoundError, ': Batch File does not exist in directory.')


# Day of the week check -- used in Weekly only
def weekday_check(day):
    weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    if day.upper()[:3] in weekdays:
        return True

    else:
        print(SyntaxError, 'Error with day of the week')

def mth_day(day):
    mth_variables = list(range(1,32))

    if day in mth_variables:
        return True
    else:
        print (SyntaxError, 'Day entered for the month is not valid.')

class Schedule():


    def daily(taskName, batchFile, startTime):

        '''Generates batch file for a daily event that requires
        name of the batch file
        batchfile you want to run
        start time (must be 24hour clock)'''

        time = is_time_format(startTime) # Returns true if startTime is in 24h clock

        file_check = file_exists(batchFile) # Returns boolean after checking if file exists in directory.


        if time == True and file_check == True:
            print ('Create Batch File')

            with open(taskName+'.bat', 'w') as batchfile:

                output = ('SchTasks /create /SC Daily /TN {0} /TR {1} /ST {2}'.format\
                       (taskName, batchFile, startTime))
                print (str(output), file=batchfile)

            p = Popen(taskName+'.bat', cwd=str(folder))
            stdout, stderr = p.communicate()

            os.remove(taskName+'.bat')

            with open (taskName + ' delete.bat', 'w') as delBatch:

                output = 'SchTasks /Delete /TN {0}'.format(taskName)
                print (str(output), file=delBatch)
                
        elif is_time_format(startTime) == False:
            print (SyntaxError, ': Time must be entered in 24 hour clock.')        


    def weekly(taskName, batchFile, day, startTime):

        '''Generates batch file for a weekly event that requires
        name of the batch file
        batchfile you want to run
        day (MON,TUE etc)
        start time (must be 24hour clock)'''

        day = day.upper()[:3]

        time = is_time_format(startTime) # Returns true if startTime is in 24h clock

        file_check = file_exists(batchFile) # Returns boolean after checking if file exists in directory.

        day_check = weekday_check(day)

        if time == True and file_check == True and day_check == True:
            print ('Create Batch File')

            with open (taskName+'.bat', 'w') as batchfile:

                output = ('SchTasks /create /SC WEEKLY /D {0} /TN {1} /TR {2} /ST {3}'\
                          .format(day, taskName, batchFile, startTime))
                print (str(output), file=batchfile)

            p = Popen(taskName+'.bat', cwd=str(folder))
            stdout, stderr = p.communicate()

            os.remove(taskName+'.bat')

            with open (taskName + ' delete.bat', 'w') as delBatch:

                output = 'SchTasks /Delete /TN {0}'.format(taskName)
                print (str(output), file=delBatch)

        elif is_time_format(startTime) == False:
            print (SyntaxError, ': Time must be entered in 24 hour clock.')



    def monthly(taskName, batchFile, day, startTime):

        '''Generates batch file for a monthly event that requires
        name of the batch file
        batchfile you want to run
        day (as a number)
        start time (must be 24hour clock)'''

        time = is_time_format(startTime) # Returns true if startTime is in 24h clock

        file_check = file_exists(batchFile) # Returns boolean after checking if file exists in directory.

        day_chk = mth_day(int(day)) # Checks that the day is valid.
        
        if time == True and file_check == True and day_chk == True:
            print ('Create Batch File')

            with open (taskName+'.bat', 'w') as batchfile:

                output = ('SchTasks /create /SC MONTHLY /D {0} /TN {1} /TR {2} /ST {3}'\
                          .format(day, taskName, batchFile, startTime))
                print (str(output),'\npause', file=batchfile)

            p = Popen(taskName+'.bat', cwd=str(folder))
            stdout, stderr = p.communicate()

            os.remove(taskName+'.bat')

            with open (taskName + ' delete.bat', 'w') as delBatch:

                output = 'SchTasks /Delete /TN {0}'.format(taskName)
                print (str(output), file=delBatch)

        elif is_time_format(startTime) == False:
            print (SyntaxError, ': Time must be entered in 24 hour clock.')
