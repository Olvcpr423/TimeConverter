# Function UTCExcTab_OrigintoUTC, used to calculate the time difference between the "input" and UTC.
# This file ia a part of "TimeConverter.py", removing this file will cause the main program stop working.
# Author: Olvcpr423.

# Start:

def OrigintoUTC(input):
    if input == '0':
        return int(0)
    elif input == '+1' or input == '-1':
        if input == '+1':
            return int(-3600)
        elif input == '-1':
            return int(+3600)
    elif input == '+2' or input == '-2':
        if input == '+2':
            return int(-7200)
        elif input == '-2':
            return int(+7200)
    elif input == '+3' or input == '-3':
        if input == '+3':
            return int(-10800)
        elif input == '-3':
            return int(+10800)
    elif input == '+3:30' or input == '-3:30':
        if input == '+3:30':
            return int(-12600)
        elif input == '-3:30':
            return int(+12600)
    elif input == '+4' or input == '-4':
        if input == '+4':
            return int(-14400)
        elif input == '-4':
            return int(+14400)
    elif input == '+5' or input == '-5':
        if input == '+5':
            return int(-18000)
        elif input == '-5':
            return int(+18000)
    elif input == '+6' or input == '-6':
        if input == '+6':
            return int(-21600)
        elif input == '-6':
            return int(+21600)
    elif input == '+7' or input == '-7':
        if input == '+7':
            return int(-25200)
        elif input == '-7':
            return int(+25200)
    elif input == '+8' or input == '-8':
        if input == '+8':
            return int(-28800)
        elif input == '-8':
            return int(+28800)
    elif input == '+9' or input == '-9':
        if input == '+9':
            return int(-32400)
        elif input == '-9':
            return int(+32400)
    elif input == '+9:30' or input == '-9:30':
        if input == '+9:30':
            return int(-34200)
        elif input == '-9:30':
            return int(+34200)
    elif input == '+10' or input == '-10':
        if input == '+10':
            return int(-36000)
        elif input == '-10':
            return int(+36000)
    elif input == '+11' or input == '-11':
        if input == '+11':
            return int(-39600)
        elif input == '-11':
            return int(+39600)
    elif input == '+12' or input == '-12':
        if input == '+12':
            return int(-43200)
        elif input == '-12':
            return int(+43200)

    elif input == '+4:30':
        return int(-16200)
    elif input == '+5:30':
        return int(-19800)
    elif input == '+5:45':
        return int(-20700)
    elif input == '+6:30':
        return int(-23400)
    elif input == '+9:30':
        return int(-34200)
    elif input == '+10:30':
        return int(-37800)
    elif input == '+12:45':
        return int(-45900)
    elif input == '+13':
        return int(-46800)
    elif input == '+14':
        return int(-50400)

# End.
