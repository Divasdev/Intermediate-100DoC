
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
#
# data_dict={
#     "students":["amy","divas","sharma"],
#     "scores":[76,45,35]
# }
#
#
# data=pandas.DataFrame(data_dict)
#
# data.to_csv("new_data.csv")
# print(data)
#


data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260124.csv")
grey=len(data[data["Primary Fur Color"]=="Gray"])
red=len(data[data["Primary Fur Color"]=="Cinnamon"])
black=len(data[data["Primary Fur Color"]=="Black"])
print(grey)
print(red)
print(black)


data_dit={
    "Fur Color":["Grey","Cinnamon","Black"],

    "count":[grey,red,black]


}

df=pandas.DataFrame(data_dit)
df.to_csv("sq_count.csv")

