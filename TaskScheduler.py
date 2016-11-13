# Next step is to enter in some validation to restrict waht fields can contain,
# and to be unable to produce invalid batch files. 


import time, os
from subprocess import Popen

folder = os.getcwd()
        
'''Generates batch file for a daily event that requires
name of the batch file
batchfile you want to run
start time (must be 24hour clock)'''

def daily(taskName, batchFile, startTime):
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

'''Generates batch file for a weekly event that requires
name of the batch file
batchfile you want to run
day (MON,TUE etc)
start time (must be 24hour clock)'''


def weekly(taskName, batchFile, day, startTime):
    with open (taskName+'.bat', 'w') as batchfile:

        output = ('SchTasks /create /SC WEEKLY /D {0} /TN {1} /TR {2} /ST {3}'\
                  .format(day, taskName, batchFile, startTime))
        print (str(output),'\npause', file=batchfile)

    p = Popen(taskName+'.bat', cwd=str(folder))
    stdout, stderr = p.communicate()

    os.remove(taskName+'.bat')

    with open (taskName + ' delete.bat', 'w') as delBatch:

        output = 'SchTasks /Delete /TN {0}'.format(taskName)
        print (str(output), file=delBatch)


'''Generates batch file for a monthly event that requires
name of the batch file
batchfile you want to run
day (as a number)
start time (must be 24hour clock)'''

def monthly(taskName, batchFile, month, startTime):
    with open (taskName+'.bat', 'w') as batchfile:

        output = ('SchTasks /create /SC WEEKLY /D {0} /TN {1} /TR {2} /ST {3}'\
                  .format(day, taskName, batchfile, startTime))
        print (str(output), file=batchFile)

    p = Popen(taskName+'.bat', cwd=str(folder))
    stdout, stderr = p.communicate()

    os.remove(taskName+'.bat')

    with open (taskName + ' delete.bat', 'w') as delBatch:

        output = 'SchTasks /Delete /TN {0}'.format(taskName)
        print (str(output), file=delBatch)

