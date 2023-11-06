# FileNotFound error
# from builtins import FileNotFoundError
#
# try:
#     file = open("file.txt")
#     a_dictionary = {"key": "value"}
#     value = a_dictionary["key"]
# except FileNotFoundError as error_message:
#     print(f"file deosn't exists {error_message}")
#     file = open("file.txt", 'w')
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key does not exists? {error_message}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     print("hey man")
#     file.close()
# KeyError


# IndexError
# text = "abc"
# print(text + 5)

# age = 200
#
# if age>110:
#     raise TypeError("Yo! man this is not a valid age")
#


# fruits = eval(input())

fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error_message:
        print(error_message)
    else:
        print(fruit + " Pie")


make_pie(1)

# eval() function will create a list of dictionaries using the input

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError as error_message:
        pass
