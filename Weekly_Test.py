def weekly(day):
    day = day[:3]
    print ('Day [:3]', day)
    day = day.upper()
    print ('Day.upper:', day)
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
        
weekly('mon')
monthly(31)
