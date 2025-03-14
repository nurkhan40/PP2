"""
Python Datetime
"""
"""
#-----------------------------------------------------
import datetime

x = datetime.datetime.now()
print(x)
#-----------------------------------------------------
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
#-----------------------------------------------------
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
#-----------------------------------------------------
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
#-----------------------------------------------------
"""

print("----------------------------------------------------------------------------------------")
print('Python Datetime')

print("----------------------------------------------------------------------------------------")
print('Example 1: Getting Current Date and Time')

import datetime

x = datetime.datetime.now()
print('import datetime')
print('x = datetime.datetime.now()')
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 2: Extracting Year and Weekday')

import datetime

x = datetime.datetime.now()

print('import datetime')
print('x = datetime.datetime.now()')
print('print(x.year)')
print('print(x.strftime("%A"))')
print(x.year)
print(x.strftime("%A"))

print("----------------------------------------------------------------------------------------")
print('Example 3: Creating a Specific Date')

import datetime

x = datetime.datetime(2020, 5, 17)

print('import datetime')
print('x = datetime.datetime(2020, 5, 17)')
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 4: Formatting a Date')

import datetime

x = datetime.datetime(2018, 6, 1)

print('import datetime')
print('x = datetime.datetime(2018, 6, 1)')
print('print(x.strftime("%B"))')
print(x.strftime("%B"))

print("----------------------------------------------------------------------------------------")


"""
Directive	    Description	                                                        Example
%a	            Weekday, short version	                                            Wed	
%A	            Weekday, full version	                                            Wednesday	
%w	            Weekday as a number 0-6, 0 is Sunday	                            3	
%d	            Day of month 01-31	                                                31	
%b	            Month name, short version	                                        Dec	
%B	            Month name, full version	                                        December	
%m	            Month as a number 01-12	                                            12	
%y	            Year, short version, without century	                            18	
%Y	            Year, full version	                                                2018	
%H	            Hour 00-23	                                                        17	
%I	            Hour 00-12	                                                        05	
%p	            AM/PM	                                                            PM	
%M	            Minute 00-59	                                                    41	
%S	            Second 00-59	                                                    08	
%f	            Microsecond 000000-999999	                                        548513	
%z	            UTC offset	                                                        +0100	
%Z	            Timezone	                                                        CST	
%j	            Day number of year 001-366	                                        365	
%U	            Week number of year, Sunday as the first day of week, 00-53	        52	
%W	            Week number of year, Monday as the first day of week, 00-53	        52	
%c	            Local version of date and time	                                    Mon Dec 31 17:41:00 2018	
%C	            Century	                                                            20	
%x	            Local version of date	                                            12/31/18	
%X	            Local version of time	                                            17:41:00	
%%	            A % character	                                                    %	
%G	            ISO 8601 year	                                                    2018	
%u	            ISO 8601 weekday (1-7)	                                            1	
%V	            ISO 8601 weeknumber (01-53)                                     	01
"""
