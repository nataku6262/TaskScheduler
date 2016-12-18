import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32': base = 'Win32GUI'

opts = {'include_files':["C:\\Users\Gavin\Documents\GitHub\TaskScheduler\TaskScheduler.py"].['C:\\Users\Gavin\Documents\GitHub\TaskScheduler\pyBatch.bat']}

setup ( name='Py TaskSchedule',
        version= '1.0',
        description = 'TaskScheduler',
        author = 'Gavin White',
        options = {'build_exe': build_exe_options}
        executables = [Executable('TaskScheduler.py', shortcutName= 'Py TaskSchedule',
                                  shortcutDir = 'DesktopFolder', base=base)])
        
