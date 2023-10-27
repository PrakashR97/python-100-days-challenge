# data = []
#
# with open("weather_data.csv", 'r') as csv_data:
#     for csv in csv_data:
#         data.append(csv.strip())
#
# print(data)

# with open("weather_data.csv", 'r') as csv_data:
#     data = csv_data.readlines()
#     print(data)

# output
# ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(sum(temp_list) / len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# monday_data = (data[data.day == 'Monday'])
# print(data[data.temp == data["temp"].max()])
# print(monday_data.temp[0])
# f = (9 / 5 * (int(monday_data.temp[0]))) + 32
# print(f)

# Create dataframe from scratch
# data_dict = {"students": ["Prakash", "James", "Angela"],
#              "scores": [76, 56, 56]
#              }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data_dict = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data = data_dict.to_dict()
# print(    squirrel_data)

gray_colors = data_dict[data_dict["Primary Fur Color"] == 'Gray']
gray_count = gray_colors["Primary Fur Color"].count()
red_colors = data_dict[data_dict["Primary Fur Color"] == 'Red']
red_count = red_colors["Primary Fur Color"].count()
black_colors = data_dict[data_dict["Primary Fur Color"] == 'Black']
black_count = black_colors["Primary Fur Color"].count()
cinnamon_colors = data_dict[data_dict["Primary Fur Color"] == 'Cinnamon']
cinnamon_count = cinnamon_colors["Primary Fur Color"].count()

squirrel_data = {"color": ["gray", "red", "black", "cinnamon"],
                 "count": [gray_count, red_count, black_count, cinnamon_count]}

df = pandas.DataFrame(squirrel_data)
df.to_csv("squirrel_count.csv")

# data = squirrel_data["Primary Fur Color"]
# gray = []
# black = []
# red = []
# for i in data:
#     if str(data[i]).lower() == "gray":
#         gray.append(data[i])
#     if str(data[i]).lower() == "black":
#         black.append(data[i])
#     if str(data[i]).lower() == "red":
#         red.append(data[i])
#
# squirrel_dict_data = {
#     "Fur color": ["gray", "black", "red"],
#     "Count": [len(gray), len(black), len(red)]
# }
#
# squirrel = pandas.DataFrame(squirrel_dict_data)
# squirrel.to_csv("squirrel_count.csv")
