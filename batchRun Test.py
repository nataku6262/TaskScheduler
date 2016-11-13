import os

folder = os.getcwd()
##exec(open(str(folder) +'\\task.bat').read())
##

from subprocess import Popen
p = Popen("task.bat", cwd=str(folder))
stdout, stderr = p.communicate()
