import os

def file_exists(file):
    folder, file = file.rsplit('/' or '\\',1)
    chk_folder = os.listdir(folder)
    if file in chk_folder:
        True
    else:
        print (FileNotFoundError)
    
    #print ('Folder:', folder, '\nFile:', file, '\nDirectory List:', chk_folder)

file_exists('C:/Users/Gavin/Documents/GitHub/TaskScheduler/pyBatch.ba')
    
#file1 = 'C:/Users/Gavin/Documents/GitHub/TaskScheduler'

#print (file1.rsplit('/', 1))
