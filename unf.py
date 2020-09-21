import time
import UTCExcTab_OrigintoUTC
import UTCExcTab_UTCtoTarget

Origintimezone = input('Please enter the Origin Timezone') # Get "Origin Time's Timezone".
if Origintimezone = 'Z':
    OrigintimeTS = time.time()
else:
    
Origintime = input('Please enter the Origin Time') # Get "Origin Time".
OrigintimeTS = time.mktime(time.strptime(Origintime, "%Y-%m-%d %H:%M:%S")) # Turn "Origin Time" into timestamp.
OrigintimezonetoUTC = float(UTCExcTab_OrigintoUTC.OrigintoUTC(Origintimezone)) # Get the time difference between "Origin Time's Timezone" and UTC.
print(OrigintimezonetoUTC)
Targettimezone = input('Please enter the Target Timezone') # Get "Target Time's Timezone".
UTCtoTargettimezone = float(UTCExcTab_UTCtoTarget.UTCtoTarget(Targettimezone)) # Get the time difference between UTC and "Target Time's Timezone".
print(UTCtoTargettimezone)
DiffOriginnTarget = OrigintimezonetoUTC + UTCtoTargettimezone # Calc the time difference between "Origin Time's Timezone" and "Target Time's Timezone"
TargettimeTS = OrigintimeTS + DiffOriginnTarget # Calc "Targettime"'s timestamp, based on "DiffOriginTarget".
Targettime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(TargettimeTS)) # Turn "TargettimeTS" into "Target Time"
print(Targettime)
