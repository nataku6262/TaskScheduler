Initial Brief  -  09/11/2016

Purpose is to create a class that can be called in future scripts to  create a batch file that will generate a batch file that creates a task for a python script to run. 

Look in the directory for taask with the same name (if yes do nothing, else do below).
The task needs to be able to create the batch script.
Save the file.
Call the batch script to be run and create the task.
delete the batch file.

Web Page for scheduled task options 18:57 16/11/2016
https://support.microsoft.com/en-us/kb/814596#bookmark-5


24 Hour Time Error Generation - 11:28 20/11/2016

Added in error generation when the time is not provided in 24 hour clock.
For Daily, Weekly and Monthly Schedule. 

File Existence confirmation & error gen - 02:50 24/11/2016

Added in validation to cofirm that the batch file exists in the defined directory
and to generate an error if it is absent. 


DAY OF WEEK CHECK -- 10:35 26/11/2016

Added in check for day entered in weekly schedule task function


NEXT - Monthly day check (1-31) - what does windows do when 31 entered for months with only 30 days?
