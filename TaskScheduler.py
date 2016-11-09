# Creating Batch Files

class task_scheduler:
    #taskName, action, startTime
##    self.taskName = taskName
##    self.action = action
##    self.startTime = startTime

    def __init__(self, schedule):
            self.schedule = schedule

    def weekly(day):
        day = day[:3]
        day = day.upper()
        if day == 'MON' or day == 'TUE' or day == 'WED' or day == \
            'THU' or day == 'FRI' or day == 'SAT' or day == 'SUN':
            print ('/SC DAILY /D', day)
        else:
            print ('You need to define a day of the week.')

    def monthly (day):
        if day <= 31:
            print ('/SC MONTHLY /D', day)
        else:
            print ('There is not more than 31 days in any month')

    def schedule(schedule):
        schedule = schedule.upper()
        if schedule == 'DAILY':
            return '/SC DAILY'
        elif schedule == 'WEEKLY':
            weekly()
        elif schedule == 'MONTHLY':
            monthly()

    def create_task():
        with open('taskschedule.bat', 'w') as file:
            print ('SchTasks /Create {0} {1} {2} {3} {4}').format(schdule, taskName, action, startTime)
            

task_scheduler('daily')   
