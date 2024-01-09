
with open("weather_data.csv") as weather_data:
    data = weather_data.readlines()
    print(data)


import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)
temp_list = data["temp"].to_list()
print(len(temp_list))
# calculate the avg temperature
sum1 = 0
for temp in range(0, len(temp_list)):
    sum1 += temp_list[temp]
avg = sum1/len(temp_list)
print(f"Average temperature is {avg}")

# Average
print(data["temp"].mean())
# Maximum
print(data["temp"].max())

# Get row data
print(data[data.day == "Monday"])

# Get the row with the highest temperature
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp = monday_temp * 9/5 + 32
print(monday_temp)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "July"],
    "Scores": [75, 89, 87]
}

data_from_dict = pandas.DataFrame(data_dict)
print(data_from_dict)
data_from_dict.to_csv("new_data.csv")
