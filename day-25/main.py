
import pandas
# data=pandas.read_csv("weather_data.csv")
# print(type(data))
# temp_data=data["temp"]
#
# print(temp_data.max())
#
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])
#
#
# monday=data[data.day=="Monday"]
# print(monday.condition)
# mon_temp=monday.temp[0]
# mon_temp_F=mon_temp*9/5+32
# print(mon_temp_F)

data_dict={
    "students":["amy","divas","sharma"],
    "scores":[76,45,35]
}


data=pandas.DataFrame(data_dict)

data.to_csv("new_data.csv")
print(data)




