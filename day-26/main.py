#new_dict={new_key:new_value for (key,value) in dict.items()}
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list_of_words=sentence.split()
#
# result={word:len(word) for word  in list_of_words}
# print(result)


# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {day_name:((temp_c* 9/5)+32) for (day_name,temp_c) in weather_c.items()}
#
# print(weather_f)



student_dict={
    "student":["Divas","Tushar",'Raj'],
    "score":[56,78,67]
}


import pandas
student_data_frame=pandas.DataFrame(student_dict)

# print(student_data_frame)
#
#
# for (key,value) in student_data_frame.items():
#     print(value)


for (index,row) in student_data_frame.iterrows():
    if row.student=="Divas":
        print(row.score)

