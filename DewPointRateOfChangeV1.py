
import datetime
temp1 = -1.2
temp2 = 0.2 #temps

num = temp2 - temp1
hour1,min1 = 15, 0 
hour2,min2 = 15, 30
today = datetime.datetime.today()

year,month,day = today.year, today.month, today.day

t1 = datetime.datetime(year,month,day,hour1,min1)
t2 = datetime.datetime(year,month,day,hour2,min2)

den = t2 - t1
# 2. Convert timedelta to a measurable unit (like total days or seconds)
delta_in_min = den.total_seconds() / 60

# 3. Calculate Rate of Change: (Value 2 - Value 1) / Time Delta
rate_of_change =  num / delta_in_min

print(f"Start Time: {t1.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"End Time:   {t2.strftime('%Y-%m-%d %H:%M:%S')} (Interval: {delta_in_min})")
print(f"Temperature Change: {rate_of_change:+.2f} degrees")
print(f"Rate of change: {rate_of_change} degrees/min")
