# Reading File
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# Writing File
# with open("new_file.txt",mode="w") as file:
#     file.write("\nNew text.")


with open("E:\Python\python-100-days-challenge\my_file.txt", mode="r") as read_file:
    content = int(read_file.read())
    print(content)
