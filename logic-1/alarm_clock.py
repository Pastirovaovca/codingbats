# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue,
# ...6=Sat, and a boolean indicating if we are on vacation,
# return a string of the form "7:00" indicating when the
# alarm clock should ring. Weekdays, the alarm should be "7:00"
# and on the weekend it should be "10:00". Unless we are on
# vacation -- then on weekdays it should be "10:00"
# and weekends it should be "off".
#
#
# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'

def alarm_clock(day, on_vacation):



    # 0-6 = Sun-Sat
    # on_vacation = False
    #     weekday_alarm = '7:00'
    #     weekend_alarm = '10:00'
    # on_vacation = True
    #     weekday_alarm = '10:00'
    #     weekend_alarm = 'off'

    if on_vacation == False:
        if day in range(1,6):
            return '7:00'
        else:
            return '10:00'
    else:
        if day in range(1,6):
            return '10:00'
        else:
            return 'Off'

    # while on_vacation == False:
    #     if day in range(1, 6):
    #         return '7:00'
    #     else:
    #         return '10:00'
    # else:
    #     if day in range(1, 6):
    #         return '10:00'
    #     else:
    #         return 'off'



print(alarm_clock(5, False))
