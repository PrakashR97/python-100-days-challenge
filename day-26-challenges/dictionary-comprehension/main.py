import random

import pandas

names = ["Alex", "Beth", "Angela", "Prakash", "Emma"]

student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score > 50}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words = sentence.split(" ")

word_dict = {word: len(word) for word in words}
print(word_dict)

temperature = {"Monday": 13, "Tuesday": 14, "Wednesday": 15}

weather_f = {day: temp * (9 / 5) + 32 for day, temp in temperature.items()}
print(weather_f)

student_dict = {"student": ["Angela", "Prakash", "Lily"],
                "score": [56, 76, 98]}

student_data = pandas.DataFrame(student_dict)
print(student_data)

for (key, value) in student_data.iterrows():
    print(value.score)
