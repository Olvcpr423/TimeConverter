import time
import UTCExcTab_OrigintoUTC
import UTCExcTab_UTCtoTarget

print('The result is: ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(UTCExcTab_OrigintoUTC.OrigintoUTC(input('Please enter the Origin Timezone: '))) + float(UTCExcTab_UTCtoTarget.UTCtoTarget(input('Please enter the Target Timezone: '))) + time.mktime(time.strptime(input('Please enter the Origin Time: '), "%Y-%m-%d %H:%M:%S")))))

#Author: Olvcpr423