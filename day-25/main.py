
import pandas
data=pandas.read_csv("weather_data.csv")
print(type(data))
temp_data=data["temp"]

print(temp_data.max())

print(data[data.day=="Monday"])
print(data[data.temp==data.temp.max()])





