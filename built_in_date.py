from datetime import date,time,datetime,timedelta,timezone
#date
dates=date.today()
print(dates)
print("year",dates.year)
print("month",dates.month)
print("day",dates.day)
print("weekday",dates.weekday())
print("day name",dates.strftime("%A"))

#datetime
datet=datetime.now()
print(datet)
print("date",datet.date())
print("time",datet.time())

#time
#datet=datetime.now()
#datet.time()
t=datetime.now().time()
print(t)
print("hour",t.hour)
print("min",t.minute)
print("sec",t.second)
print("time format",t.strftime("%H-%M-%S"))


#strftime
#date
print("str dates",dates.strftime("%d/%m/%Y"))
print("str dates month abb",dates.strftime("%A/%B/%Y"))
print("str dates month abb half",dates.strftime("%a /%b/%Y"))
print("str datetime",datet.strftime("%Y/%m/%d--%H:%M:%S"))
print("str datetime abb full ",datet.strftime("%Y/%B/%A %H:%M:%S"))
print("str datetime abb half ",datet.strftime("%Y/%b/%a %H:%M:%S"))
print("day name",t.strftime("%H-%M-%S"))

#strptime
k="2025-2-15"
d=datetime.strptime(k,"%Y-%m-%d")

k1="2025-2-15 12"
d1=datetime.strptime(k1,"%Y-%m-%d %H")
print(d)

k2="2025-2-15 12:10:4"
d2=datetime.strptime(k2,"%Y-%m-%d %H:%M:%S")
print(d)


#date(),datetime(),time()
k=date(2025,4,4)
print(k)
y=datetime(10,2,3,3,3,3)
print(y)
z=time(12,2,2)
print(z)


#timedelta 
print("timedelta on date",dates+timedelta(days=10))
print("timedelta on datetime",datet+timedelta(days=2,hours=2,minutes=30))

#timezone-us to india-usually inn hrs mins
ist =timezone(timedelta(hours=5,minutes=30))
us=datetime(3,3,3,3,3,3,tzinfo=ist)
print(us)

#isoformat-only to date or datetiime or time objects 
k=date(2025,3,3)
print("isoformat",k.isoformat())