import datetime as dt
days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

dob = input("enter your date of birth day in the format DD/MM/YYYY")
day, month, year = dob.split("/")
date_of_birth = dt.datetime(year=int(year), month=int(month), day=int(day))
print(days[date_of_birth.weekday()])
