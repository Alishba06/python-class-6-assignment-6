
# Current time deta

# import time

# print(time.time())


# Seconds ko UTC time

# print(time.gmtime(0))



# Seconds ko local time

# print(time.localtime(time.time()))



# Getting the Current Time

# localtime = time.localtime(time.time())
# print("Local current time:" , localtime)





# Getting the Formatted Time

# localtime = time.asctime(time.localtime(time.time()))
# print("Local current time:" , localtime)


# import calendar

# print(calendar.month(2025 , 1))



# import datetime

# x = datetime.datetime(2025,1,1)

# print(x.strftime("%f"))  # Microseconds → 000000
# print(x.strftime("%A"))  # Day ka naam → Wednesday
# print(x.strftime("%Y"))  # Saal → 2025
# print(x.strftime("%B"))  # Mahina → January
